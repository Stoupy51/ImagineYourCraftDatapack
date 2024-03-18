
# Import config
from src.importer import *

# Get every vanilla IDs
vanilla_ids = []
for v in DATABASE.values():
	if v["id"] not in vanilla_ids:
		vanilla_ids.append(v["id"].replace("minecraft:", ""))

# For each vanilla ID, create the json model file
blocks = ["barrel", "command_block"]
for id in vanilla_ids:
	with super_open(f"{BUILD_RESOURCE_PACK}/assets/minecraft/models/item/{id}.json", "w") as file:
		block_or_item = "block" if id in blocks else "item"
		content = {"parent": f"{block_or_item}/{id}", "overrides": "__LIST__"}
		formatted_content = json.dumps(content, indent = '\t')

		# Get overrides
		overrides = []
		for item, data in DATABASE.items():
			if data["id"].replace("minecraft:","") == id:
				overrides.append(f'{{"predicate": {{ "custom_model_data": {data["custom_model_data"]}}}, "model": "{NAMESPACE}:{block_or_item}/{item}" }}')
		overrides = ",\n\t\t".join(overrides)

		# Write the content to the file
		file.write(formatted_content.replace('"__LIST__"', f'[\n\t\t{overrides}\n\t]') + "\n")
	pass
info("Vanilla models created")

