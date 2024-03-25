
# Imports
from src.importer import *

# Give Additional data for every item
database_additions = {
	"adamantium_ore": {
		"wiki": [
			["Description", "Adamantium Ore is a mineable ore found in the overworld caves."],
			["How to get one?", "In the overworld, anywhere below y=40"],
			["Can be mined with", "Any pickaxe"],
			["Drops", "1 Raw Adamantium (fortune enchantment is supported)"],
			["Silk Touch?", "Also supported"]
		]
	},
	"massive_obsidian_block" : {RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"misc","group":"obsidian","shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr("minecraft:obsidian")}}]},
	"obsidian_ingot" : {RESULT_OF_CRAFTING:[{"type":"smelting","result_count":1,"category":"misc","group":"obsidian","experience":0.2,"cookingtime":800,"ingredient":ingr_repr("massive_obsidian_block")}],RESULT_OF_CRAFTING:[{"type":"blasting","result_count":1,"category":"misc","group":"obsidian","experience":0.2,"cookingtime":400,"ingredient":ingr_repr("massive_obsidian_block")}]},
	"iron_furnace": {"id": CUSTOM_BLOCK_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"misc","shape":["XXX","XFX","XXX"],"ingredients":{"X":ingr_repr("minecraft:iron_ingot"),"F":ingr_repr("minecraft:furnace")}}]},
	"box_jump": {"id": CUSTOM_BLOCK_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"misc","ingredients":[ingr_repr("minecraft:oak_planks"),ingr_repr("ruby")]}]},
	"box_speed": {"id": CUSTOM_BLOCK_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"misc","ingredients":[ingr_repr("minecraft:oak_planks"),ingr_repr("sapphire")]}]},

	# Materials for food
	"beer_mug":			{"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","group":"beer_mug","shape":["XX","X X","XX"],"ingredients":{"X":ingr_repr("minecraft:glass")}},{"type":"shaped","result_count":4,"category":"misc","group":"beer_mug","shape":[" XX","X X"," XX"],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
	"caffeine":			{"id": CUSTOM_ITEM_VANILLA},
	"can":				{"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["XSX"," X"],"ingredients":{"X":ingr_repr("minecraft:iron_ingot"),"S":ingr_repr("steel_ingot")}}]},
	"cola":				{"id": CUSTOM_ITEM_VANILLA},
	"empty_glass":		{"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["X X","X X"," X"],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
	"toast":			{"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":4,"category":"misc","shape":["XXX"],"ingredients":{"X":ingr_repr("minecraft:bread")}}]},
	"hops":				{"id": CUSTOM_ITEM_VANILLA},
	"glass_pot":		{"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shaped","result_count":1,"category":"misc","shape":["X X","X X","XXX"],"ingredients":{"X":ingr_repr("minecraft:glass")}}]},
	"taurine":			{"id": CUSTOM_ITEM_VANILLA},

	# Foods
	"apple_juice":		{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:jump_boost","duration":30*20,"amplifier":0},"probability":1.0}]}, 	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("apple"),ingr_repr("empty_glass")]}]},
	"beer":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:nausea","duration":30*20,"amplifier":0},"probability":1.0}]}, 		RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("beer_mug"),ingr_repr("hops")]}]},
	"cherry":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.8}},
	"cherry_cake":		{"id": CUSTOM_BLOCK_VANILLA, 																																													RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("cherry"),ingr_repr("minecraft:cake")]}]},
	"coca":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:haste","duration":30*20,"amplifier":0},"probability":1.0}]}, 		RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("can"),ingr_repr("cola"),ingr_repr("minecraft:sugar"),ingr_repr("caffeine")]}]},
	"hot_chocolate":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":3, "saturation_modifier":0.8, "effects":[{"effect":{"id":"minecraft:speed","duration":30*20,"amplifier":0},"probability":1.0}]}, 		RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("minecraft:cocoa_beans"),ingr_repr("minecraft:bowl"),ingr_repr("minecraft:milk_bucket")]}]},
	"nutella":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":False, "nutrition":10, "saturation_modifier":0.6}, 																										RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("minecraft:cocoa_beans")]*3 + [ingr_repr("minecraft:sugar")]*2 + [ingr_repr("minecraft:milk_bucket"), ingr_repr("glass_pot")]}]},
	"nutella_toast":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":False, "nutrition":12, "saturation_modifier":0.6}, 																										RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":4,"category":"food","ingredients":[ingr_repr("nutella")] + [ingr_repr("toast")]*4}]},
	"red_bull":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:regeneration","duration":30*20,"amplifier":0},"probability":1.0}]}, 	RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":1,"category":"food","ingredients":[ingr_repr("can"), ingr_repr("taurine"), ingr_repr("minecraft:sugar"), ingr_repr("caffeine")]}]},

	# Items crafting vanilla items
	"chainmail": {"id": CUSTOM_ITEM_VANILLA, RESULT_OF_CRAFTING:[{"type":"crafting_shapeless","result_count":4,"category":"misc","ingredients":[ingr_repr("minecraft:chain")]*2}],
		USED_FOR_CRAFTING:[
			{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X"],"ingredients":{"X":ingr_repr("chainmail")},"result":ingr_repr("minecraft:chainmail_chestplate", count = 1)},
			{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","XXX","XXX"],"ingredients":{"X":ingr_repr("chainmail")},"result":ingr_repr("minecraft:chainmail_chestplate", count = 1)},
			{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X","X X"],"ingredients":{"X":ingr_repr("chainmail")},"result":ingr_repr("minecraft:chainmail_leggings", count = 1)},
			{"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","X X"],"ingredients":{"X":ingr_repr("chainmail")},"result":ingr_repr("minecraft:chainmail_boots", count = 1)},
		]
	},
}

# Update the database with new data
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v
info("Database additions loaded")

