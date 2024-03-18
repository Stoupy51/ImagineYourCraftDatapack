
# Import config
from src.importer import *

# Get every vanilla IDs
vanilla_ids = []
for v in DATABASE.values():
	if v["id"] not in vanilla_ids:
		vanilla_ids.append(v["id"].replace("minecraft:", ""))

# For each vanilla ID, create the json model file
blocks = [CUSTOM_BLOCK_VANILLA, "command_block"]
for id in vanilla_ids:
	with super_open(f"{BUILD_RESOURCE_PACK}/assets/minecraft/models/item/{id}.json", "w") as file:
		block_or_item = "block" if id in blocks else "item"
		content = {"parent": f"{block_or_item}/{id}", "overrides": []}

		# Get overrides
		for item, data in DATABASE.items():
			if data["id"].replace("minecraft:","") == id:
				content["overrides"].append({"predicate": { "custom_model_data": data["custom_model_data"]}, "model": f"{NAMESPACE}:{block_or_item}/{item}" })

		# Write the content to the file
		file.write(super_json_dump(content).replace('{"','{ "').replace('"}','" }').replace(',"', ', "') + "\n")
	pass
info("Vanilla models created")

