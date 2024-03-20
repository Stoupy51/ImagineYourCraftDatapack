
# Import config
from src.importer import *

# For each item in the database, create a loot table
for item, data in DATABASE.items():
	loot_table = {"pools":[{"rolls":1,"entries":[{"type":"minecraft:item","name": data["id"]}]}]}

	# Copy custom data from storage
	copy_custom_data = {
		"function":"minecraft:copy_custom_data",
		"source":{"type":"minecraft:storage","source":f"{NAMESPACE}:items"},
		"ops":[{"source":f"all.{item}.components.custom_data","target":"{}","op":"merge"}]
	}

	# Set components
	set_components = {"function":"minecraft:set_components","components":{}}
	for k, v in data.items():
		if k not in NOT_COMPONENTS and k != "custom_data":
			if k == "dyed_color":
				r,g,b = v//65536, (v//256)%256, v%256
				set_components["components"]["minecraft:dyed_color"] = {"rgb":(r,g,b)}
			else:
				set_components["components"][f"minecraft:{k}"] = v
	
	# Add functions
	loot_table["pools"][0]["entries"][0]["functions"] = [copy_custom_data, set_components]

	with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/loot_tables/i/{item}.json", "w") as f:
		super_json_dump(loot_table, f, max_level = -1)
	pass
info("Made loot tables for every item")


# Loot tables for items with crafting recipes
for item, data in DATABASE.items():
	if data.get(CRAFTING_RECIPES):
		results = []
		for d in data[CRAFTING_RECIPES]:
			count = d["result_count"]
			if count != 1:
				results.append(count)

		# For each result count, create a loot table for it
		for result_count in results:
			loot_table = {"pools":[{"rolls":1,"entries":[{"type":"minecraft:loot_table","name":f"{NAMESPACE}:i/{item}","functions":[{"function":"minecraft:set_count","count":result_count}]}]}]}
			with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/loot_tables/i/{item}_x{result_count}.json", "w") as f:
				super_json_dump(loot_table, f, max_level = -1)
info("Multiple counts loot tables made for every item with crafting recipes")


# TODO: give all

