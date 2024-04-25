
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *

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
			set_components["components"][f"minecraft:{k}"] = v
	
	# Add functions
	loot_table["pools"][0]["entries"][0]["functions"] = [copy_custom_data, set_components]

	with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/loot_tables/i/{item}.json", "w") as f:
		super_json_dump(loot_table, f, max_level = 9)
	pass
info("Made loot tables for every item")


# Loot tables for items with crafting recipes
for item, data in DATABASE.items():
	if data.get(RESULT_OF_CRAFTING):
		results = []
		for d in data[RESULT_OF_CRAFTING]:
			count = d["result_count"]
			if count != 1:
				results.append(count)

		# For each result count, create a loot table for it
		for result_count in results:
			loot_table = {"pools":[{"rolls":1,"entries":[{"type":"minecraft:loot_table","value":f"{NAMESPACE}:i/{item}","functions":[{"function":"minecraft:set_count","count":result_count}]}]}]}
			with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/loot_tables/i/{item}_x{result_count}.json", "w") as f:
				super_json_dump(loot_table, f, max_level = -1)
info("Multiple counts loot tables made for every item with crafting recipes")


# Make a give all command that gives chests with all the items
CHEST_SIZE = 27
total_chests = (len(DATABASE) + CHEST_SIZE - 1) // CHEST_SIZE
chests = []
database_copy = DATABASE.copy()
for i in range(total_chests):
	chest_contents = []
 
	# For each slot of the chest, append an item and remove it from the copy
	for j in range(CHEST_SIZE):
		if not database_copy:
			break
		item, data = database_copy.popitem()
		data = data.copy()
		id = data["id"]
		for k in NOT_COMPONENTS:	# Remove non-component data
			if data.get(k):
				del data[k]
		json_content = super_json_dump(data, max_level = 0).replace("\n","")
		chest_contents.append(f'{{slot:{j},item:{{count:1,id:"{id}",components:{json_content}}}}}')
	joined_content = ",".join(chest_contents)
	chests.append(f'give @s chest[container=[{joined_content}],custom_name=\'{{"text":"Chest [{i+1}/{total_chests}]","color":"yellow"}}\',lore=[\'{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}\']]')
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/_give_all.mcfunction", "w") as f:
	f.write("\n" + "\n\n".join(chests) + "\n\n")
info("Give all function successfully made")

