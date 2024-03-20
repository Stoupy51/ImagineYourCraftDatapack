
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
}

# Update the database with new data
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v
info("Database additions loaded")

