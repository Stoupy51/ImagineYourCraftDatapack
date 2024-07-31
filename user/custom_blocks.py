
# Imports
from config import *
from python_datapack.utils.database_helper import *

def main(database: dict[str, dict]):
	vanilla_blocks = {
		"adamantium_block": {VANILLA_BLOCK: {"id":"minecraft:netherite_block", "apply_facing": False}},
		"adamantium_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "adamantium_fragment"},
		"deepslate_adamantium_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "adamantium_fragment"},
		"sapphire_block": {VANILLA_BLOCK: {"id":"minecraft:diamond_block", "apply_facing": False}},
		"sapphire_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "sapphire"},
		"deepslate_sapphire_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "sapphire"},
		"ruby_block": {VANILLA_BLOCK: {"id":"minecraft:diamond_block", "apply_facing": False}},
		"ruby_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "ruby"},
		"deepslate_ruby_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "ruby"},
		"topaz_block": {VANILLA_BLOCK: {"id":"minecraft:diamond_block", "apply_facing": False}},
		"topaz_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "topaz"},
		"deepslate_topaz_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "topaz"},
		"massive_obsidian_block": {VANILLA_BLOCK: {"id":"minecraft:netherite_block", "apply_facing": False}},
		"steel_block": {VANILLA_BLOCK: {"id":"minecraft:iron_block", "apply_facing": False}},
		"steel_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "raw_steel"},
		"lignite_block": {VANILLA_BLOCK: {"id":"minecraft:coal_block", "apply_facing": False}},
		"lignite_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "lignite"},
		"slate_block": {VANILLA_BLOCK: {"id":"minecraft:coal_block", "apply_facing": False}},
		"slate_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES, NO_SILK_TOUCH_DROP: "slate"},
		"iron_furnace": {VANILLA_BLOCK: {"id":"minecraft:furnace", "apply_facing": True}},
		"box_jump": {VANILLA_BLOCK: {"id":"minecraft:oak_planks", "apply_facing": False}},
		"box_speed": {VANILLA_BLOCK: {"id":"minecraft:oak_planks", "apply_facing": False}},
		"blue_block_ctf": {VANILLA_BLOCK: {"id":"minecraft:glass", "apply_facing": False}},
		"clear_glass": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"birch_wood_lantern": {VANILLA_BLOCK: {"id":"minecraft:ochre_froglight", "apply_facing": False}},
		"jungle_wood_lantern": {VANILLA_BLOCK: {"id":"minecraft:ochre_froglight", "apply_facing": False}},
		"oak_wood_lantern": {VANILLA_BLOCK: {"id":"minecraft:ochre_froglight", "apply_facing": False}},
		"spruce_wood_lantern": {VANILLA_BLOCK: {"id":"minecraft:ochre_froglight", "apply_facing": False}},
		"iron_lantern": {VANILLA_BLOCK: {"id":"minecraft:ochre_froglight", "apply_facing": False}},
		"red_light": {VANILLA_BLOCK: {"id":"minecraft:red_concrete", "apply_facing": False}},
		"reversed_oak_planks": {VANILLA_BLOCK: {"id":"minecraft:oak_planks", "apply_facing": False}},
		"cherry_cake": {VANILLA_BLOCK: {"id":"minecraft:cake", "apply_facing": False}},
		"nuclear_bomb": {VANILLA_BLOCK: {"id":"minecraft:tnt", "apply_facing": False}},

		# Items using item_frame for placing
		"cloud": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"flatware": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"hops_seeds": {VANILLA_BLOCK: {"id":"minecraft:wheat", "apply_facing": False}},
		"iron_ladder": {VANILLA_BLOCK: {"id":"minecraft:ladder", "apply_facing": True}},
		"black_flower": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"blue_flower": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"white_flower": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"blob": {VANILLA_BLOCK: {"id":"minecraft:structure_void", "apply_facing": False}},
		"lignite_torch": {VANILLA_BLOCK: {"id":"minecraft:torch", "apply_facing": False}},
	}

	# Merge this dict with the database
	for k, v in vanilla_blocks.items():
		if k in database:
			database[k].update(v)
		else:
			database[k] = v

