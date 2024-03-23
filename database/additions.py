
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


	# Foods
	"apple_juice":		{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":"minecraft:absorption","duration":30*20,"amplifier":0,"probability":1.0}]}},
	"beer":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":"minecraft:nausea","duration":30*20,"amplifier":0,"probability":1.0}]}},
	"cherry":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.8}},
	"cherry_cake":		{"id": CUSTOM_BLOCK_VANILLA},
	"coca":				{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":"minecraft:strength","duration":30*20,"amplifier":0,"probability":1.0}]}},
	"hot_chocolate":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":3, "saturation_modifier":0.8, "effects":[{"effect":"minecraft:speed","duration":30*20,"amplifier":0,"probability":1.0}]}},
	"nutella_toast":	{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":4, "saturation_modifier":0.6, "effects":[{"effect":"minecraft:resistance","duration":30*20,"amplifier":0,"probability":1.0}]}},
	"red_bull":			{"id": CUSTOM_ITEM_VANILLA, "food":{"can_always_eat":True, "nutrition":2, "saturation_modifier":0.6, "effects":[{"effect":"minecraft:regeneration","duration":30*20,"amplifier":0,"probability":1.0}]}},
}

# Update the database with new data
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v
info("Database additions loaded")

