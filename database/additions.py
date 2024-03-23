
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
	"iron_furnace": {"id": CUSTOM_BLOCK_VANILLA},

	# Materials for food
	"beer_mug":			{"id": CUSTOM_ITEM_VANILLA, CRAFTING_RECIPES:[{"type":"shaped","result_count":4,"shape":"XX X XXX ","ingredients":{"X":ingr_repr("minecraft:glass")}},{"type":"shaped","result_count":4,"shape":" XXX X XX","ingredients":{"X":ingr_repr("minecraft:glass")}}]},
	"caffeine":			{"id": CUSTOM_ITEM_VANILLA},
	"can":				{"id": CUSTOM_ITEM_VANILLA, CRAFTING_RECIPES:[{"type":"shaped","result_count":4,"shape":"XSX X ","ingredients":{"X":ingr_repr("minecraft:iron_ingot"),"S":ingr_repr("steel_ingot")}}]},
	"cola":				{"id": CUSTOM_ITEM_VANILLA},
	"empty_glass":		{"id": CUSTOM_ITEM_VANILLA, CRAFTING_RECIPES:[{"type":"shaped","result_count":4,"shape":"X XX X X ","ingredients":{"X":ingr_repr("minecraft:iron_ingot")}}]},
	"toast":			{"id": CUSTOM_ITEM_VANILLA, CRAFTING_RECIPES:[{"type":"shaped","result_count":4,"shape":"XXX","ingredients":{"X":ingr_repr("minecraft:bread")}}]},
	"hops":				{"id": CUSTOM_ITEM_VANILLA},
	"glass_pot":		{"id": CUSTOM_ITEM_VANILLA, CRAFTING_RECIPES:[{"type":"shaped","result_count":1,"shape":"X XX XXXX","ingredients":{"X":ingr_repr("minecraft:glass")}}]},
	"taurine":			{"id": CUSTOM_ITEM_VANILLA},

	# Foods
	"apple_juice":		{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:jump_boost","duration":30*20,"amplifier":0},"probability":1.0}]}, 	CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("apple", count = 1), ingr_repr("empty_glass", count = 1)]}]},
	"beer":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:nausea","duration":30*20,"amplifier":0},"probability":1.0}]}, 		CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("beer_mug", count = 1), ingr_repr("hops", count = 1)]}]},
	"cherry":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.8}},
	"cherry_cake":		{"id": CUSTOM_BLOCK_VANILLA, 																																													CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("cherry", count = 1), ingr_repr("minecraft:cake", count = 1)]}]},
	"coca":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:haste","duration":30*20,"amplifier":0},"probability":1.0}]}, 		CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("can", count = 1), ingr_repr("cola", count = 1), ingr_repr("minecraft:sugar", count = 1), ingr_repr("caffeine", count = 1)]}]},
	"hot_chocolate":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":3, "saturation_modifier":0.8, "effects":[{"effect":{"id":"minecraft:speed","duration":30*20,"amplifier":0},"probability":1.0}]}, 		CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("minecraft:cocoa_beans", count = 1), ingr_repr("minecraft:bowl", count = 1), ingr_repr("minecraft:milk_bucket", count = 1)]}]},
	"nutella":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":False, "nutrition":10, "saturation_modifier":0.6}, 																										CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("minecraft:cocoa_beans", count = 3), ingr_repr("minecraft:sugar", count = 2), ingr_repr("minecraft:milk_bucket", count = 1), ingr_repr("glass_pot", count = 1)]}]},
	"nutella_toast":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":False, "nutrition":12, "saturation_modifier":0.6}, 																										CRAFTING_RECIPES:[{"type":"shapeless","result_count":4,"ingredients":[ingr_repr("nutella", count = 1), ingr_repr("toast", count = 4)]}]},
	"red_bull":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":{"id":"minecraft:regeneration","duration":30*20,"amplifier":0},"probability":1.0}]}, 	CRAFTING_RECIPES:[{"type":"shapeless","result_count":1,"ingredients":[ingr_repr("can", count = 1), ingr_repr("taurine", count = 1), ingr_repr("minecraft:sugar", count = 1), ingr_repr("caffeine", count = 1)]}]},
}

# Update the database with new data
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v
info("Database additions loaded")

