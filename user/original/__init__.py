""" Beet plugin giving every `OriginalBlock` its converted models, its items definition, and the functions keeping its display in step with its host.

Runs after `stewbeet.plugins.datapack.custom_blocks`, whose place and destroy functions it extends.
"""
# Imports
from beet import Context, ItemModel, Model, Texture
from stewbeet import (
	Block,
	BlockTag,
	Mem,
	advancement_entity,
	loot_condition,
	set_json_encoder,
	write_advancement,
	write_function,
	write_load_file,
	write_predicate,
	write_versioned_function,
)
from stouputils.typing import JsonDict

from .blocks import Interaction, OriginalBlock, Schema
from .models import ModelConverter, inflated_model
from .sync import SyncWriter, Variant, read_variants

# Constants
PLACED_FACING: dict[Schema, tuple[str, str, str, str]] = {
	Schema.STAIRS: ("south", "west", "north", "east"),
	Schema.GATE: ("south", "west", "north", "east"),
	Schema.TRAPDOOR: ("north", "east", "south", "west"),
}
""" Host `facing` for each `#rotation` score (1 is a player looking south), as vanilla places these blocks. """

NOT_CONNECTABLE: list[str] = [
	"#minecraft:air", "minecraft:barrier", "minecraft:short_grass", "minecraft:tall_grass", "minecraft:fern", "minecraft:snow_block",
	"minecraft:fire", "minecraft:soul_fire", "#minecraft:flowers", "#minecraft:saplings",
]
""" Neighbours lamps and rods do not attach to: air, plants, snow and fire, as `gt_1` and `hb_1` decide. """


# Main function
def beet_default(ctx: Context) -> None:
	converter = ModelConverter()
	writer = SyncWriter()
	follows: dict[str, str] = {}
	for block in OriginalBlock.all():
		variants: list[Variant] = read_variants(block, converter)
		roles: list[str] = list(dict.fromkeys(v.model for v in variants))
		if block.inventory_model:
			legacy: bool = block.inventory_model.startswith("legacy/")
			converter.convert(block.inventory_model.removeprefix("legacy/") if legacy else f"iyc:{block.inventory_model}", in_blockstate=True)
		write_items_definition(ctx, block, roles)
		tree: str = writer.tree(block, variants, roles)
		if block.schema.follows_host:
			follows[tree] = f"iyc.tree.{tree.split('/')[-1]}"
		write_placement(block, tree, follows.get(tree, ""))
		write_destroy(block)

	for model_id, model in converter.models.items():
		Mem.ctx.assets.models[model_id] = set_json_encoder(Model(inflated_model(model)), max_level=3)
	for texture_id, source in converter.textures.items():
		Mem.ctx.assets.textures[texture_id] = Texture(source_path=source)

	hosts: dict[str, list[str]] = {}
	for block in OriginalBlock.all():
		hosts.setdefault(block.host_tag.removeprefix("#iyc:"), []).append(block.host.split("[")[0])
	for path, values in hosts.items():
		Mem.ctx.data["iyc"].block_tags[path] = set_json_encoder(BlockTag({"values": sorted(set(values))}))
	Mem.ctx.data["iyc"].block_tags["not_connectable"] = set_json_encoder(BlockTag({"values": NOT_CONNECTABLE}))

	write_load_file("scoreboard objectives add iyc.shape dummy\n")
	write_aim()
	write_versioned_function("second", "execute as @e[type=item_display,tag=iyc.follow] at @s run function iyc:shapes/follow\n")
	write_function("iyc:shapes/follow", "".join(
		f"execute if entity @s[tag={tag}] run return run function {tree}\n" for tree, tag in follows.items()
	))
	write_interactions()


# Functions
def write_items_definition(ctx: Context, block: OriginalBlock, roles: list[str]) -> None:
	""" Show each model of the block from the role its display stores, and the inventory model everywhere else. """
	tints: JsonDict = {} if block.color is None else {"tints": [{"type": "minecraft:custom_model_data", "index": 0, "default": 16777215}]}
	definition: JsonDict = {"model": {
		"type": "minecraft:select",
		"property": "minecraft:custom_model_data",
		"index": 0,
		"cases": [{"when": str(i), "model": {"type": "minecraft:model", "model": model, **tints}} for i, model in enumerate(roles)],
		"fallback": {"type": "minecraft:model", "model": f"iyc:item/{block.id}", **tints},
	}}
	Mem.ctx.assets.item_models[f"iyc:{block.id}"] = set_json_encoder(ItemModel(definition), max_level=5)


def write_placement(block: OriginalBlock, tree: str, follow_tag: str) -> None:
	""" Give the freshly placed display its tags, its host the state vanilla would have placed, its interaction, and its first look. """
	content: str = "\n# Original model\ntag @s add iyc.original\nscoreboard players set @s iyc.shape -1\n"
	if follow_tag:
		content += f"tag @s add iyc.follow\ntag @s add {follow_tag}\n"
	if block.connects_to:
		content += f"tag @s add iyc.connect.{block.connects_to}\n"
	content += "".join(f"tag @s add iyc.{tag}\n" for tag in block.tags)
	if block.color is not None:
		content += f'data modify entity @s item.components."minecraft:custom_model_data" set value {{colors:[{block.color}]}}\n'
	content += host_state_lines(block)
	if block.interaction:
		content += interaction_summon(block, block.interaction)
	write_function(block_function(block, "place_secondary"), content + f"function {tree}\n")


def host_state_lines(block: OriginalBlock) -> str:
	""" Commands setting the host's facing from the placer's look and its half from where the placer clicked, as vanilla does. """
	if block.schema not in (*PLACED_FACING, Schema.SLAB, Schema.SLOPE):
		return ""

	host: str = block.host
	lines: list[str] = ["function iyc:placing/aim"]
	if block.schema == Schema.SLAB:
		lines.append(f"execute if score #upper iyc.data matches 1 run setblock ~ ~ ~ {host}[type=top]")

	for rotation, facing in enumerate(PLACED_FACING.get(block.schema, ()), start=1):
		if block.schema == Schema.GATE:
			lines.append(f"execute if score #rotation iyc.data matches {rotation} run setblock ~ ~ ~ {host}[facing={facing}]")
			continue
		for upper, half in ((0, "bottom"), (1, "top")):
			lines.append(
				f"execute if score #rotation iyc.data matches {rotation} if score #upper iyc.data matches {upper} "
				f"run setblock ~ ~ ~ {host}[facing={facing},half={half}]"
			)
	return "\n".join(lines) + "\n"


def interaction_summon(block: OriginalBlock, interaction: Interaction) -> str:
	""" The interaction standing on the block bottom, a little larger than the block so it is targeted before the host. """
	tags: list[str] = ["iyc.interaction"]
	if interaction.seat is not None:
		tags.append(f"iyc.seat.{round(interaction.seat * 100)}")
	tags.extend(f"iyc.{tag}" for tag in block.tags if tag.startswith("lights."))
	return (
		f"summon interaction ~ ~-0.5 ~ {{width:{interaction.width}f,height:{interaction.height}f,response:true,"
		f"Tags:[{','.join(f'\"{tag}\"' for tag in tags)}]}}\n"
	)


def write_destroy(block: OriginalBlock) -> None:
	""" Turn what the host drops into this block's item, or drop it when it was broken through its interaction. """
	if block.foreign_drop:
		write_function(
			block_function(block, "destroy"),
			f'execute as @n[type=item,nbt={{Item:{{id:"{block.foreign_drop}"}}}},distance=..1] run function {block_function(block, "foreign_drop")}\n',
			prepend=True,
		)
		write_function(
			block_function(block, "foreign_drop"),
			f"data modify entity @s Item.count set value 1\nfunction {Block.from_id(block.drops or block.id).functions['replace_item']}\n",
		)
	if block.hand_drop:
		host: str = block.host.split("[")[0]
		write_function(block_function(block, "destroy"), (
			f'execute unless entity @n[type=item,nbt={{Item:{{id:"{host}"}}}},distance=..1] '
			f"if entity @p[distance=..8,gamemode=survival] run loot spawn ~ ~ ~ loot iyc:i/{block.id}\n"
		), prepend=True)
	if block.interaction:
		write_function(block_function(block, "destroy"), (
			f"execute if score #break_drop iyc.data matches 1 run loot spawn ~ ~ ~ loot iyc:i/{block.drops or block.id}\n"
			"kill @e[type=interaction,tag=iyc.interaction,distance=..0.6]\n"
		))


def write_aim() -> None:
	""" `iyc:placing/aim`, run as an entity at the center of a block being placed, tells where the look of the `iyc.placer` player hits it.

	`#upper` ends at 1 when the look leaves the block through its upper half, which is how vanilla picks top slabs and stairs,
	and `#floor` at 1 when it leaves through the bottom face, the player having clicked the top of the block below.
	"""
	write_function("iyc:placing/aim", """
tag @s add iyc.placing
scoreboard players set #upper iyc.data 0
scoreboard players set #floor iyc.data 0
scoreboard players set #inside iyc.data 0
scoreboard players set #steps iyc.data 0
execute as @p[tag=iyc.placer] at @s anchored eyes positioned ^ ^ ^ anchored feet run function iyc:placing/ray
tag @s remove iyc.placing
""")
	write_function("iyc:placing/ray", """
# A box test from 0.5 below a point holds when the point is in the block, from 1 below when it is in its upper half
scoreboard players add #steps iyc.data 1
execute if score #steps iyc.data matches 120.. run return 0
scoreboard players operation #was_inside iyc.data = #inside iyc.data
execute positioned ~-0.5 ~-0.5 ~-0.5 store success score #inside iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #inside iyc.data matches 1 positioned ~-0.5 ~-1 ~-0.5 store success score #upper iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #was_inside iyc.data matches 1 if score #inside iyc.data matches 0 positioned ~-0.5 ~0.5 ~-0.5 store success score #floor iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #was_inside iyc.data matches 1 if score #inside iyc.data matches 0 run return 0
execute positioned ^ ^ ^0.05 run function iyc:placing/ray
""")


def block_function(block: OriginalBlock, name: str) -> str:
	return Block.from_id(block.id).functions[name]


def write_interactions() -> None:
	""" Breaking an interaction block by hitting it, sitting on a seat, and lighting a lamp with flint and steel. """
	interaction: JsonDict = advancement_entity({"entity_type": "minecraft:interaction", "nbt": '{Tags:["iyc.interaction"]}'})
	write_advancement("iyc:interaction/attacked", {
		"criteria": {"requirement": {"trigger": "minecraft:player_hurt_entity", "conditions": {
			"entity": interaction,
		}}},
		"rewards": {"function": "iyc:interaction/attacked"},
	})
	write_function("iyc:interaction/attacked", """
advancement revoke @s only iyc:interaction/attacked
execute store success score #break_drop iyc.data if entity @s[gamemode=!creative]
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s attack at @s align xyz positioned ~0.5 ~0.5 ~0.5 run function iyc:interaction/break
scoreboard players set #break_drop iyc.data 0
""")
	write_function("iyc:interaction/break", """
setblock ~ ~ ~ air
execute as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] run function iyc:custom_blocks/destroy
""")

	write_advancement("iyc:interaction/used", {
		"criteria": {"requirement": {"trigger": "minecraft:player_interacted_with_entity", "conditions": {
			"entity": interaction,
		}}},
		"rewards": {"function": "iyc:interaction/used"},
	})
	write_function("iyc:interaction/used", """
advancement revoke @s only iyc:interaction/used
tag @s add iyc.user
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s interaction at @s run function iyc:interaction/use
tag @s remove iyc.user
""")
	seats: set[float] = {b.interaction.seat for b in OriginalBlock.all() if b.interaction and b.interaction.seat is not None}
	lamps: list[str] = sorted({tag for b in OriginalBlock.all() for tag in b.tags if tag.startswith("lights.")})
	write_function("iyc:interaction/use", "data remove entity @s interaction\n" + "".join(
		f"execute if entity @s[tag=iyc.seat.{round(seat * 100)}] unless entity @p[tag=iyc.user,predicate=iyc:has_vehicle] "
		f"run return run function iyc:interaction/sit {{height:{seat}}}\n"
		for seat in sorted(seats)
	) + "".join(
		f"execute if entity @s[tag=iyc.{tag}] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel "
		f"align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {{lit:\"{tag.removeprefix('lights.')}\"}}\n"
		for tag in lamps
	))
	write_function("iyc:interaction/sit", """
$execute positioned ~ ~$(height) ~ summon item_display run tag @s add iyc.seat
ride @p[tag=iyc.user] mount @n[type=item_display,tag=iyc.seat]
""")
	write_function("iyc:interaction/light", """
setblock ~ ~ ~ air
execute as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] run function iyc:custom_blocks/destroy
$function iyc:custom_blocks/$(lit)/place_main
""")
	write_predicate("iyc:has_passenger", loot_condition("minecraft:entity_properties", entity="this", predicate={"passenger": {}}))
	write_versioned_function("tick", "execute as @e[type=item_display,tag=iyc.seat,predicate=!iyc:has_passenger] run kill @s\n")

