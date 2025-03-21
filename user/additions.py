
# Imports
import stouputils as stp
from python_datapack.utils.database_helper import *
from config import NAMESPACE

def main(database: dict[str, dict]) -> dict[str, dict]:

	# Give Additional data for every item
	MISC = "miscellaneous"
	database_additions = {
		"adamantium_ore": {
			WIKI_COMPONENT: [
				{"text":"Description: "},		{"text":"Adamantium Ore is a mineable ore found in the overworld caves.\n","color":"gray"},
				{"text":"How to get one? "},	{"text":"In the overworld, anywhere below y=40.\n","color":"gray"},
				{"text":"Can be mined with: "},	{"text":"Any pickaxe.\n","color":"gray"},
				{"text":"Drops: "},				{"text":"1 Raw Adamantium (fortune enchantment is supported)\n","color":"gray"},
				{"text":"Silk Touch? "},		{"text":"Also supported","color":"gray"},
			]
		},
		"adamantium_fragment": {
			WIKI_COMPONENT: [
				{"text":"Description: "},		{"text":"Adamantium Fragment is a material used to craft Adamantium stuff.\n","color":"gray"},
				{"text":"How to get one? "},	{"text":"By mining Adamantium Ore.","color":"gray"},
			]
		},
		"massive_obsidian_block" : {"id": CUSTOM_BLOCK_VANILLA, "category": "material", RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"misc","group":"obsidian","ingredients":[ingr_repr("minecraft:obsidian")] * 9}]},
		"obsidian_ingot" : {RESULT_OF_CRAFTING:[{"type":"smelting","result_count":1,"category":"misc","group":"obsidian","experience":0.2,"cookingtime":800,"ingredient":ingr_repr("massive_obsidian_block", NAMESPACE)},{"type":"blasting","result_count":1,"category":"misc","group":"obsidian","experience":0.2,"cookingtime":400,"ingredient":ingr_repr("massive_obsidian_block", NAMESPACE)}]},
		"iron_furnace": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",			RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"misc","shape":["XXX","XFX","XXX"],"ingredients":{"X":ingr_repr("minecraft:iron_ingot"),"F":ingr_repr("minecraft:furnace")}}]},
		"box_jump": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",				RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"misc","ingredients":[ingr_repr("minecraft:oak_planks"),ingr_repr("ruby", NAMESPACE)]}]},
		"box_speed": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",				RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"misc","ingredients":[ingr_repr("minecraft:oak_planks"),ingr_repr("sapphire", NAMESPACE)]}]},
		"blue_block_ctf": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",		RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":8,"category":"misc","shape":["XXX","XGX","XXX"],"ingredients":{"X":ingr_repr("minecraft:blue_wool"),"G":ingr_repr("minecraft:glass")}}]},
		"bolt": {"id": "minecraft:arrow", CATEGORY: "equipment",					"lore": [{"text":"x1.5 damage arrow","color":"gray","italic":False}], RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"equipment","ingredients":[ingr_repr("minecraft:iron_ingot"),ingr_repr("minecraft:arrow")]}]},
		"clear_glass": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",			RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":4,"category":"misc","ingredients":[ingr_repr("minecraft:glass")]*9}]},
		"cloud": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building"},
		"flatware": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building"},
		"helice_hat": {"id": "minecraft:leather_helmet", CATEGORY: "equipment",		"lore": [{"text":"A hat that makes you fly","color":"gray","italic":False}], RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"equipment","ingredients":[ingr_repr("minecraft:iron_ingot"),ingr_repr("minecraft:elytra")]}], "attribute_modifiers":[{"type":"gravity","amount":-0.09,"operation":"add_value","slot":"head","id":"iyc:gravity.head"}]},
		"hops_seeds": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "material"},
		"iron_ladder": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building",		RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["X X","XXX","X X"],"ingredients":{"X":ingr_repr("minecraft:iron_ingot")}}]},
		"l118a": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: "equipment",					"lore": [{"text":"Uses steel nuggets as bullets","color":"gray","italic":False}], RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X  "," XX"," XS"],"ingredients":{"X":ingr_repr("steel_ingot", NAMESPACE),"S":ingr_repr("slate", NAMESPACE)}}]},
		"birch_wood_lantern": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","group":"wood_lantern","ingredients":[ingr_repr("minecraft:glowstone"),ingr_repr("minecraft:birch_wood")]}]},
		"jungle_wood_lantern": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","group":"wood_lantern","ingredients":[ingr_repr("minecraft:glowstone"),ingr_repr("minecraft:jungle_wood")]}]},
		"oak_wood_lantern": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",		RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","group":"wood_lantern","ingredients":[ingr_repr("minecraft:glowstone"),ingr_repr("minecraft:oak_wood")]}]},
		"spruce_wood_lantern": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","group":"wood_lantern","ingredients":[ingr_repr("minecraft:glowstone"),ingr_repr("minecraft:spruce_wood")]}]},
		"iron_lantern": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",			RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","ingredients":[ingr_repr("minecraft:glowstone"),ingr_repr("minecraft:iron_block")]}]},
		"red_light": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",				RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"blocks","ingredients":[ingr_repr("minecraft:redstone_lamp"),ingr_repr("minecraft:red_wool")]}]},
		"reversed_oak_planks": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "building",	RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"blocks","shape":[" X","XX","X "],"ingredients":{"X":ingr_repr("minecraft:oak_planks")}}]},
		"sw1911": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: "equipment",				"lore": [{"text":"Uses steel nuggets as bullets","color":"gray","italic":False}], RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["SX ","  X"," X "],"ingredients":{"X":ingr_repr("steel_ingot", NAMESPACE),"S":ingr_repr("slate", NAMESPACE)}}]},
		"black_flower": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building"},
		"blue_flower": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building"},
		"white_flower": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: "building"},

		# Materials for food
		"beer_mug":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material",	RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","group":"beer_mug","shape":["XX ","X X","XX "],"ingredients":{"X":ingr_repr("minecraft:glass")}},{"type":"crafting_shaped","result_count":4,"category":"misc","group":"beer_mug","shape":[" XX","X X"," XX"],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
		"caffeine":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material"},
		"can":				{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material",	RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["XSX"," X "],"ingredients":{"X":ingr_repr("minecraft:iron_ingot"),"S":ingr_repr("steel_ingot", NAMESPACE)}}]},
		"cola":				{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material"},
		"empty_glass":		{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material",	RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["X X","X X"," X "],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
		"toast":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food",		RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["XXX"],"ingredients":{"X":ingr_repr("minecraft:bread")}}]},
		"hops":				{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material"},
		"glass_pot":		{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material",	RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"misc","shape":["X X","X X","XXX"],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
		"taurine":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material"},

		# Foods
		"apple_juice":		{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":2,	"saturation":0.6},		"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:jump_boost", "duration": 30*20, "amplifier": 0}]}]},	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("minecraft:apple"),ingr_repr("empty_glass", NAMESPACE)]}]},
		"beer":				{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":2,	"saturation":0.6},		"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:nausea", "duration": 30*20, "amplifier": 0}]}]},		RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("beer_mug", NAMESPACE),ingr_repr("hops", NAMESPACE)]}]},
		"cherry":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":2,	"saturation":0.8}},
		"cherry_cake":		{"id": CUSTOM_BLOCK_VANILLA, CATEGORY: "food", OVERRIDE_MODEL: {"parent":"block/cake"}, 																																															RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("cherry", NAMESPACE),ingr_repr("minecraft:cake")]}]},
		"coca":				{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":2,	"saturation":0.6},		"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:haste", "duration": 30*20, "amplifier": 0}]}]},			RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("can", NAMESPACE),ingr_repr("cola", NAMESPACE),ingr_repr("minecraft:sugar"),ingr_repr("caffeine", NAMESPACE)]}]},
		"hot_chocolate":	{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":3,	"saturation":0.8},		"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:speed", "duration": 30*20, "amplifier": 0}]}]},			RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("minecraft:cocoa_beans"),ingr_repr("minecraft:bowl"),ingr_repr("minecraft:milk_bucket")]}]},
		"nutella":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":False, "nutrition":10,	"saturation":0.6},	"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:regeneration", "duration": 30*20, "amplifier": 0}]}]}, 																											RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("minecraft:cocoa_beans")]*3 + [ingr_repr("minecraft:sugar")]*2 + [ingr_repr("minecraft:milk_bucket"), ingr_repr("glass_pot", NAMESPACE)]}]},
		"nutella_toast":	{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":False, "nutrition":12,	"saturation":0.6},	"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:regeneration", "duration": 30*20, "amplifier": 0}]}]}, 																											RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":4,"category":"food","ingredients":[ingr_repr("nutella", NAMESPACE)] + [ingr_repr("toast", NAMESPACE)]*4}]},
		"red_bull":			{"id": CUSTOM_ITEM_VANILLA, CATEGORY: "food", "food":{"can_always_eat":True, "nutrition":2,	"saturation":0.6},		"consumable": {"on_consume_effects": [{"type": "minecraft:apply_effects", "effects": [{"id": "minecraft:regeneration", "duration": 30*20, "amplifier": 0}]}]}, 	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("can", NAMESPACE), ingr_repr("taurine", NAMESPACE), ingr_repr("minecraft:sugar"), ingr_repr("caffeine", NAMESPACE)]}]},

		# Items crafting vanilla items
		"chainmail": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: "material",	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":4,"category":"misc","ingredients":[ingr_repr("minecraft:chain")]*2}],
			USED_FOR_CRAFTING:[
				{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X"],"ingredients":{"X":ingr_repr("chainmail", NAMESPACE)},"result":ingr_repr("minecraft:chainmail_helmet", count = 1)},
				{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","XXX","XXX"],"ingredients":{"X":ingr_repr("chainmail", NAMESPACE)},"result":ingr_repr("minecraft:chainmail_chestplate", count = 1)},
				{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X","X X"],"ingredients":{"X":ingr_repr("chainmail", NAMESPACE)},"result":ingr_repr("minecraft:chainmail_leggings", count = 1)},
				{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","X X"],"ingredients":{"X":ingr_repr("chainmail", NAMESPACE)},"result":ingr_repr("minecraft:chainmail_boots", count = 1)},
			]
		},

		# Miscellaneous
		"blank": {"id": CUSTOM_ITEM_VANILLA},
		"blob": {"id": CUSTOM_BLOCK_ALTERNATIVE},
		"lignite_torch": {"id": CUSTOM_BLOCK_ALTERNATIVE, CATEGORY: MISC,			RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"blocks","shape":["X","S"],"ingredients":{"S":ingr_repr("minecraft:stick"),"X":ingr_repr("lignite", NAMESPACE)}}]},
		"coin": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: MISC},
		"nuclear_bomb": {"id": CUSTOM_BLOCK_VANILLA, CATEGORY: MISC,				"lore": [{"text":"Power of 5 TNTs","color":"gray","italic":False}], RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"blocks","shape":[" X ","XTX","XXX"],"ingredients":{"X":ingr_repr("minecraft:tnt"),"T":ingr_repr("topaz", NAMESPACE)}}]},
		"quiver": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: MISC},
		"rock": {"id": "minecraft:snowball", CATEGORY: MISC, "max_stack_size": 99,	"lore": [{"text":"Can be thrown","color":"gray","italic":False}]},
		"screwdriver": {"id": CUSTOM_ITEM_VANILLA, CATEGORY: MISC},
		"old_ruby": {"id": CUSTOM_ITEM_VANILLA},
	}

	# Update the database with new data
	for k, v in database_additions.items():
		if k in database:
			database[k].update(v)
		else:
			database[k] = v
	stp.info("Database additions loaded")
	return database

