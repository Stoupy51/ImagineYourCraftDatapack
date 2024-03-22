
# Import config
from src.importer import *
from database.additions import *

# Get every vanilla IDs
vanilla_ids = []
for v in DATABASE.values():
	if v["id"] not in vanilla_ids:
		vanilla_ids.append(v["id"].replace("minecraft:", ""))
	pass

"""{
    "parent": "item/handheld",
  	"textures": {
    	"layer0": "item/leather_chestplate",
    	"layer1": "item/leather_chestplate_overlay"
  	},
"""

# For each vanilla ID, create the json model file
blocks = [CUSTOM_BLOCK_VANILLA, CUSTOM_ITEM_VANILLA]
blocks = [x.replace("minecraft:", "") for x in blocks]
for id in vanilla_ids:
	with super_open(f"{BUILD_RESOURCE_PACK}/assets/minecraft/models/item/{id}.json", "w") as file:
		block_or_item = "block" if id in blocks else "item"
		if id == CUSTOM_ITEM_VANILLA.replace("minecraft:", ""):
			content = {"parent": f"block/{id}"}
			block_or_item = "item"
		else:
			content = {"parent": f"{block_or_item}/{id}"}
		if id not in blocks:
			content["parent"] = "item/handheld"
			content["textures"] = {"layer0": f"item/{id}"}
			if id in ["leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots"]:
				content["textures"]["layer1"] = f"item/{id}_overlay"

		# Get overrides
		content["overrides"] = []
		for item, data in DATABASE.items():
			if data["id"].replace("minecraft:","") == id:
				content["overrides"].append({"predicate": { "custom_model_data": data["custom_model_data"]}, "model": f"{NAMESPACE}:{block_or_item}/{item}" })

				# Additionally, add a "_on" model if there is
				if os.path.exists(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/models/{block_or_item}/{item}_on.json"):
					content["overrides"].append({"predicate": { "custom_model_data": data["custom_model_data"] + 1}, "model": f"{NAMESPACE}:{block_or_item}/{item}_on" })

		# Write the content to the file
		file.write(super_json_dump(content).replace('{"','{ "').replace('"}','" }').replace(',"', ', "') + "\n")
	pass
info("Vanilla models created")

