""" Behaviours of the mod's blocks and world generation, run once every block function exists. """
# Imports
from stewbeet import (
	Block,
	BlockTag,
	Context,
	CustomOreGeneration,
	EntityTypeTag,
	LootTable,
	Mem,
	set_json_encoder,
	write_function,
	write_load_file,
	write_tick_file,
)

from user.definitions.special import EFFECT_GENERATORS
from user.definitions.tweaks import write_tweaks

# Constants
GEM_ORES: dict[str, int] = {"ruby": 12, "sapphire": 13, "topaz": 11, "adamantium": 9}
""" Gem ores and the height above the bottom of the world their veins reach (`td_1`: one vein per chunk). """

REGION_CHUNKS: int = 36
""" Chunks in a 96x96 Smart Ore Generation region. """

NOT_LIVING: list[str] = [
	"minecraft:item_display", "minecraft:block_display", "minecraft:text_display", "minecraft:interaction", "minecraft:marker",
	"minecraft:item", "minecraft:experience_orb", "minecraft:painting", "minecraft:item_frame", "minecraft:glow_item_frame",
	"minecraft:armor_stand", "minecraft:falling_block", "minecraft:tnt", "minecraft:area_effect_cloud", "minecraft:end_crystal",
	"minecraft:minecart", "minecraft:chest_minecart", "minecraft:furnace_minecart", "minecraft:hopper_minecart", "minecraft:tnt_minecart",
	"minecraft:spawner_minecart", "minecraft:command_block_minecart", "#minecraft:boat", "#minecraft:arrows", "#minecraft:impact_projectiles",
]
""" Entities that are not mobs, left alone by the jump box, the clouds and the flowers. """

PARTICLES: dict[str, str] = {
	"black_smoke": "smoke ~ ~0.5 ~ 0 0 0 0 10",
	"portal": "portal ~ ~0.5 ~ 0 0 0 0.5 5",
	"explosion": "explosion ~ ~0.5 ~ 0 0 0 0 1",
	"white_smoke": "poof ~ ~0.5 ~ 0 0 0 0 10",
	"lava": "lava ~ ~0.5 ~ 0 0 0 0 1",
	"water": "splash ~ ~0.5 ~ 0 0 0 0 10",
	"big_black_smoke": "large_smoke ~ ~1 ~ 0.3 0.3 0.3 0 10",
	"heart": "heart ~ ~0.7 ~ 0 0 0 0 1",
}
""" What each effect generator (`gm_1`) emits above itself, every second. """


# Main function
def beet_default(ctx: Context) -> None:
	write_tick_file("""
# Check for rocks
execute if score #rock_markers iyc.data matches 1.. as @e[tag=iyc.rock_marker,predicate=!iyc:has_vehicle] at @s positioned ~ ~-0.5 ~ run function iyc:entity/rock_check/marker_final
execute as @e[type=snowball,tag=!iyc.rock_checked] run function iyc:entity/rock_check/main

# Clouds and flowers touched by living entities, players cancelling their fall through slow falling since their fall distance is read only
execute as @a[gamemode=!spectator] at @s if block ~ ~ ~ minecraft:structure_void if entity @e[type=item_display,tag=iyc.cloud,distance=..0.9] run effect give @s minecraft:slow_falling 1 0 true
execute as @a[gamemode=!spectator,gamemode=!creative] at @s if block ~ ~ ~ minecraft:tripwire run function iyc:flowers/touch
execute as @e[type=!player,type=!#iyc:not_living] at @s if block ~ ~ ~ #iyc:touched_hosts run function iyc:mob_touch

# Stairs, slopes and slabs standing on a barrier climbed without jumping, as their own collision allowed
execute as @a[tag=!iyc.stepping] at @s if entity @e[type=item_display,tag=iyc.step,distance=..1.8] run function iyc:step/enter
execute as @a[tag=iyc.stepping] at @s unless entity @e[type=item_display,tag=iyc.step,distance=..1.8] run function iyc:step/leave

# Jump box launches
execute as @a[tag=iyc.launched] run function iyc:jump_box/flight
""")
	ore_generation()
	flowers(ctx)
	touching_mobs()
	jump_boxes()
	barrier_steps()
	wall_torches()
	write_tweaks()
	for kind in EFFECT_GENERATORS:
		write_function(Block.from_id(f"{kind}_effect_generator").functions.second, f"particle {PARTICLES[kind]}\n")
	write_function(Block.from_id("nuclear_bomb").functions.destroy, "execute as @e[type=tnt,distance=..1,tag=!iyc.bomb] run function iyc:bomb/prime\n")
	write_function("iyc:bomb/prime", """
# Lit by hand or redstone it keeps most of its 80 tick fuse, set off by another explosion it was given 10 to 30
tag @s add iyc.bomb
execute store result score #fuse iyc.data run data get entity @s fuse
execute if score #fuse iyc.data matches 60.. run data modify entity @s fuse set value 120s
execute if score #fuse iyc.data matches ..59 store result entity @s fuse short 1 run random value 15..44
data modify entity @s explosion_power set value 12.0f
""")
	ctx.data["iyc"].loot_tables["seeds/hops"] = set_json_encoder(LootTable({"pools": [
		{"rolls": 1, "entries": [
			{"type": "minecraft:loot_table", "value": "iyc:i/hops", "weight": 5},
			{"type": "minecraft:loot_table", "value": "iyc:i/caffeine", "weight": 1},
		]},
		{"rolls": 3, "entries": [{"type": "minecraft:loot_table", "value": "iyc:i/hops_seeds", "weight": 8}, {"type": "minecraft:empty", "weight": 7}]},
	]}), max_level=4)


# Functions
def ore_generation() -> None:
	""" Gem ores at the bottom of the world, slate in the upper stone, steel and lignite hanging under the Nether's netherrack. """
	configs: dict[str | Block, list[CustomOreGeneration]] = {}
	for gem, height in GEM_ORES.items():
		for ore in (f"{gem}_ore", f"deepslate_{gem}_ore"):
			configs[ore] = [CustomOreGeneration(
				dimensions=["minecraft:overworld"], minimum_height=-64, maximum_height=-64 + height, veins_per_region=REGION_CHUNKS, vein_size_logic=0.4,
			)]
	configs["slate_ore"] = [CustomOreGeneration(
		dimensions=["minecraft:overworld"], minimum_height=60, maximum_height=128, veins_per_region=10 * REGION_CHUNKS, vein_size_logic=0.6,
	)]
	for ore in ("steel_ore", "lignite_ore"):
		configs[ore] = [CustomOreGeneration(
			dimensions=["minecraft:the_nether"], minimum_height=4, maximum_height=124, veins_per_region=2 * REGION_CHUNKS, vein_size_logic=1.4,
			provider=["minecraft:air"], block_conditions=["if block ~ ~1 ~ minecraft:netherrack"],
		)]
	CustomOreGeneration.all_with_config(configs)


def flowers(ctx: Context) -> None:
	""" Flower patches on grass (`td_1` gives each vanilla flower attempt a 1/4 chance per custom flower), and what touching them does. """
	CustomOreGeneration.all_with_config({flower: [CustomOreGeneration(
		dimensions=["minecraft:overworld"], minimum_height=50, maximum_height=200, veins_per_region=REGION_CHUNKS / 2, vein_size_logic=2.0,
		provider=["minecraft:air"], block_conditions=["if block ~ ~-1 ~ minecraft:grass_block"],
	)] for flower in ("blue_flower", "white_flower", "black_flower")})
	write_function("iyc:flowers/touch", """
# Poison and slowness last 100 ticks, 150 in normal and 300 in hard (gc_1, hm_1)
execute store result score #difficulty iyc.data run difficulty
execute if entity @e[type=item_display,tag=iyc.blue_flower,distance=..0.9] run function iyc:flowers/effect {effect:"poison"}
execute if entity @e[type=item_display,tag=iyc.white_flower,distance=..0.9] run function iyc:flowers/effect {effect:"slowness"}
execute if entity @e[type=item_display,tag=iyc.black_flower,distance=..0.9] run damage @s 1 minecraft:cactus
""")
	write_function("iyc:flowers/effect", """
$execute if score #difficulty iyc.data matches ..1 run effect give @s minecraft:$(effect) 5 0
$execute if score #difficulty iyc.data matches 2 run effect give @s minecraft:$(effect) 8 0
$execute if score #difficulty iyc.data matches 3 run effect give @s minecraft:$(effect) 15 0
""")


def touching_mobs() -> None:
	""" Mobs touching a flower get its effect and mobs in a cloud lose their fall distance, as every living entity did in the mod. """
	Mem.ctx.data["iyc"].entity_type_tags["not_living"] = set_json_encoder(EntityTypeTag({"values": NOT_LIVING}))
	Mem.ctx.data["iyc"].block_tags["touched_hosts"] = set_json_encoder(BlockTag({"values": ["minecraft:tripwire", "minecraft:structure_void"]}))
	write_function("iyc:mob_touch", """
execute if block ~ ~ ~ minecraft:tripwire run return run function iyc:flowers/touch
execute if entity @e[type=item_display,tag=iyc.cloud,distance=..0.9] run data modify entity @s fall_distance set value 0.0d
""")


def jump_boxes() -> None:
	""" The jump box (`gs_1`) throws whoever stands on it upward, and the datapack's speed box speeds them up. """
	write_load_file("scoreboard objectives add iyc.jump dummy\n")
	write_function(Block.from_id("box_jump").functions.tick, """
execute positioned ~-0.5 ~0.5 ~-0.5 as @a[dx=0,dy=0,dz=0,tag=!iyc.launched,gamemode=!spectator] run function iyc:jump_box/launch
execute positioned ~-0.5 ~0.5 ~-0.5 as @e[type=!player,type=!#iyc:not_living,dx=0,dy=0,dz=0] run data modify entity @s Motion[1] set value 4.0d
""")
	write_function("iyc:jump_box/launch", """
# Players move on their own client, so they are lifted by levitation: 4 ticks at amplifier 127 end near the 4 blocks per tick mobs get
playsound minecraft:block.piston.extend block @a ~ ~ ~ 0.5 0.7
effect give @s minecraft:levitation 1 127 true
attribute @s minecraft:safe_fall_distance modifier add iyc:jump_box 72 add_value
scoreboard players set @s iyc.jump 4
tag @s add iyc.launched
""")
	write_function("iyc:jump_box/flight", """
scoreboard players remove @s iyc.jump 1
execute if score @s iyc.jump matches 0 run effect clear @s minecraft:levitation
execute if score @s iyc.jump matches ..-5 if predicate {type:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_on_ground:true}}} run function iyc:jump_box/landed
""")
	write_function("iyc:jump_box/landed", "attribute @s minecraft:safe_fall_distance modifier remove iyc:jump_box\ntag @s remove iyc.launched\n")
	write_function(Block.from_id("box_speed").functions.tick, (
		"execute positioned ~-0.5 ~0.5 ~-0.5 as @a[dx=0,dy=0,dz=0,gamemode=!spectator] run effect give @s minecraft:speed 1 2 true\n"
	))


def barrier_steps() -> None:
	""" Players near a stairs, slope or slab standing on a barrier step a full block up, so they walk onto it as onto the original. """
	write_function("iyc:step/enter", "attribute @s minecraft:step_height modifier add iyc:step 0.5 add_value\ntag @s add iyc.stepping\n")
	write_function("iyc:step/leave", "attribute @s minecraft:step_height modifier remove iyc:step\ntag @s remove iyc.stepping\n")


def wall_torches() -> None:
	""" A lignite torch placed against the side of a block becomes the wall one, a vanilla wall torch being another block. """
	write_function(Block.from_id("lignite_torch").functions.place_main, f"""
tag @s add iyc.placer
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon minecraft:marker run function iyc:custom_blocks/_aim/main
execute if score #floor iyc.data matches 0 run return run function {Block.from_id("lignite_wall_torch").functions.place_main}
""", prepend=True)

