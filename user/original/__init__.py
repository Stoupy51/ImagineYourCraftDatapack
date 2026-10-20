""" Beet plugin giving every `OriginalBlock` its converted models, its items definition, and the functions keeping its display in step with its host.

Runs after `stewbeet.plugins.datapack.custom_blocks`, whose place and destroy functions it extends.
"""
# Imports
from beet import Context, ItemModel, Model, Texture
from stewbeet import (
	Block,
	BlockTag,
	Mem,
	model_with_margin,
	set_json_encoder,
	write_function,
	write_load_file,
	write_versioned_function,
)
from stouputils.typing import JsonDict

from .blocks import OriginalBlock, Schema
from .models import ModelConverter
from .sync import SyncWriter, Variant, read_variants

# Constants
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
		roles: list[str] = convert_models(block, converter, variants)
		write_items_definition(ctx, block, roles)
		tree: str = writer.tree(block, variants, roles)
		if block.schema.follows_host:
			follows[tree] = f"iyc.tree.{tree.split('/')[-1]}"
		write_placement(block, tree, follows.get(tree, ""))
		write_destroy(block)

	for model_id, model in converter.models.items():
		Mem.ctx.assets.models[model_id] = set_json_encoder(Model(model_with_margin(model)), max_level=3)
	for texture_id, source in converter.textures.items():
		Mem.ctx.assets.textures[texture_id] = Texture(source_path=source)

	hosts: dict[str, list[str]] = {}
	for block in OriginalBlock.all():
		hosts.setdefault(block.host_tag.removeprefix("#iyc:"), []).append(block.host.split("[")[0])
	for path, values in hosts.items():
		Mem.ctx.data["iyc"].block_tags[path] = set_json_encoder(BlockTag({"values": sorted(set(values))}))
	Mem.ctx.data["iyc"].block_tags["not_connectable"] = set_json_encoder(BlockTag({"values": NOT_CONNECTABLE}))

	write_load_file("scoreboard objectives add iyc.shape dummy\n")
	write_versioned_function("second", "execute as @e[type=item_display,tag=iyc.follow] at @s run function iyc:shapes/follow\n")
	write_function("iyc:shapes/follow", "".join(
		f"execute if entity @s[tag={tag}] run return run function {tree}\n" for tree, tag in follows.items()
	))
	write_lamp_lighting()


# Functions
def convert_models(block: OriginalBlock, converter: ModelConverter, variants: list[Variant]) -> list[str]:
	""" Convert the inventory model of the block, and return the distinct models its variants show, drawn at full light for an emissive block. """
	roles: list[str] = list(dict.fromkeys(v.model for v in variants))
	if block.inventory_model:
		legacy: bool = block.inventory_model.startswith("legacy/")
		converter.convert(block.inventory_model.removeprefix("legacy/") if legacy else f"iyc:{block.inventory_model}", in_blockstate=True)
	for model in roles if block.emissive else []:
		converter.emissive(model)
	return roles


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
	""" Give the freshly placed display its tags and its first look, a slope reading where the placer clicked. """
	content: str = "\n# Original model\ntag @s add iyc.original\nscoreboard players set @s iyc.shape -1\n"
	if follow_tag:
		content += f"tag @s add iyc.follow\ntag @s add {follow_tag}\n"
	if block.connects_to:
		content += f"tag @s add iyc.connect.{block.connects_to}\n"
	content += "".join(f"tag @s add iyc.{tag}\n" for tag in block.tags)
	if block.color is not None:
		content += f'data modify entity @s item.components."minecraft:custom_model_data" set value {{colors:[{block.color}]}}\n'
	if block.schema == Schema.SLOPE:
		content += "execute summon marker run function iyc:custom_blocks/_aim/main\n"
	write_function(block_function(block, "place_secondary"), content + f"function {tree}\n")


def write_destroy(block: OriginalBlock) -> None:
	""" Turn what the host drops into this block's item. """
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


def block_function(block: OriginalBlock, name: str) -> str:
	return Block.from_id(block.id).functions[name]


def write_lamp_lighting() -> None:
	""" Using flint and steel on a lamp's interaction replaces the lamp by its lit counterpart, dropping nothing. """
	write_function("iyc:custom_blocks/_interaction/use", "".join(
		f"execute if entity @s[tag=iyc.{block.id}] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel "
		"align xyz positioned ~0.5 ~0.5 ~0.5 "
		f"run return run function iyc:interaction/light {{lit:\"{tag.removeprefix('lights.')}\"}}\n"
		for block in OriginalBlock.all() for tag in block.tags if tag.startswith("lights.")
	))
	write_function("iyc:interaction/light", """
scoreboard players set #no_drop iyc.data 1
function iyc:custom_blocks/_interaction/break
$function iyc:custom_blocks/$(lit)/place_main
""")

