
# Imports
from src.config import *

#
vanilla_blocks = {
	"adamantium_block": {VANILLA_BLOCK: "minecraft:netherite_block"},
	"adamantium_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"sapphire_block": {VANILLA_BLOCK: "minecraft:diamond_block"},
	"sapphire_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"ruby_block": {VANILLA_BLOCK: "minecraft:diamond_block"},
	"ruby_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"topaz_block": {VANILLA_BLOCK: "minecraft:diamond_block"},
	"topaz_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"massive_obsidian_block": {VANILLA_BLOCK: "minecraft:netherite_block"},
	"steel_block": {VANILLA_BLOCK: "minecraft:iron_block"},
	"steel_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"lignite_block": {VANILLA_BLOCK: "minecraft:coal_block"},
	"lignite_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"slate_block": {VANILLA_BLOCK: "minecraft:coal_block"},
	"slate_ore": {VANILLA_BLOCK: VANILLA_BLOCK_FOR_ORES},
	"iron_furnace": {VANILLA_BLOCK: {"id":"minecraft:furnace", "block_states":["facing"]}},
	"box_jump": {VANILLA_BLOCK: "minecraft:oak_planks"},
	"box_speed": {VANILLA_BLOCK: "minecraft:oak_planks"},
	"blue_block_ctf": {VANILLA_BLOCK: "minecraft:glass"},
	"clear_glass": {VANILLA_BLOCK: "minecraft:structure_void"},
	"birch_wood_lantern": {VANILLA_BLOCK: "minecraft:ochre_froglight"},
	"jungle_wood_lantern": {VANILLA_BLOCK: "minecraft:ochre_froglight"},
	"oak_wood_lantern": {VANILLA_BLOCK: "minecraft:ochre_froglight"},
	"spruce_wood_lantern": {VANILLA_BLOCK: "minecraft:ochre_froglight"},
	"iron_lantern": {VANILLA_BLOCK: "minecraft:ochre_froglight"},
	"red_light": {VANILLA_BLOCK: "minecraft:red_concrete"},
	"reversed_oak_planks": {VANILLA_BLOCK: "minecraft:oak_planks"},
	"cherry_cake": {VANILLA_BLOCK: "minecraft:cake"},
	"nuclear_bomb": {VANILLA_BLOCK: "minecraft:tnt"},

	# Items using item_frame for placing
	"cloud": {VANILLA_BLOCK: "minecraft:structure_void"},
	"flatware": {VANILLA_BLOCK: "minecraft:structure_void"},
	"hops_seeds": {VANILLA_BLOCK: "minecraft:wheat"},
	"iron_ladder": {VANILLA_BLOCK: "minecraft:ladder"},
	"black_flower": {VANILLA_BLOCK: "minecraft:structure_void"},
	"blue_flower": {VANILLA_BLOCK: "minecraft:structure_void"},
	"white_flower": {VANILLA_BLOCK: "minecraft:structure_void"},
	"blob": {VANILLA_BLOCK: "minecraft:structure_void"},
	"lignite_torch": {VANILLA_BLOCK: "minecraft:torch"},
}

# Merge this dict with the database
for k, v in vanilla_blocks.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v

