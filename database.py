
# This file contains every single details about the items and blocks data, it is used to generate every datapack file
# Everything stored in a dictionnary. This python script should be imported
from src.config import *

# Get every item texture paths from textures folder
textures_filenames = [f for f in os.listdir(TEXTURES_FOLDER) if os.path.isfile(os.path.join(TEXTURES_FOLDER, f))]

# Generate ores
ores = ["adamantium", "emerald", "massive_obsidian", "ruby", "sapphire", "topaz", "steel", "lignite"]
placeables = ["block", "ore"]
ingredients = ["ingot", "nugget", "dust", "fragment", "raw", ""]
armors = ["helmet", "chestplate", "leggings", "boots"]
for ore in ores:
	material = ore.replace("massive_","")

	# Placeables
	for placeable in placeables:
		block = f"{ore}_{placeable}"
		if f"{block}.png" not in textures_filenames: # Skip if the block doesn't have a texture
			continue
		block_str = block.replace("_"," ").title()
		if any(block in texture for texture in textures_filenames):
			DATABASE[block] = {}
			DATABASE[block]["id"] = CUSTOM_BLOCK_VANILLA	# Item for placing custom block
			DATABASE[block]["smithed"] = {}
			DATABASE[block]["smithed"]["dict"] = {"block": {ore: 1}}
			if placeable == "ore":
				DATABASE[block]["smithed"]["dict"]["ore"] = {material: 1}
			DATABASE[block]["smithed"]["ignore"] = {"functionality": 1, "crafting": 1} # As it's a custom block, we don't want the CUSTOM_BLOCK_VANILLA to be used
			DATABASE[block]["display"] = {}
			DATABASE[block]["display"]["Name"] = f'[{{"text":"{block_str}","italic":false,"color":"white"}}]'
			DATABASE[block]["display"]["Lore"] = [f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]']
			DATABASE[block][NAMESPACE] = {block:1}
		
		# Crafting 9x ingot into block
		DATABASE[block]["result_of_crafting"] = []
		if placeable == "block":
			if f"{material}_ingot.png" in textures_filenames:
				DATABASE[block]["result_of_crafting"].append(str({"type":"shapeless", "result_count": 1, "ingredients": [{"Count":9, "custom_data":f"{NAMESPACE}.{ore}_ingot"}]}))
			if f"{material}_fragment.png" in textures_filenames:
				DATABASE[block]["result_of_crafting"].append(str({"type":"shapeless", "result_count": 1, "ingredients": [{"Count":9, "custom_data":f"{NAMESPACE}.{ore}_fragment"}]}))
			if f"{material}.png" in textures_filenames:
				DATABASE[block]["result_of_crafting"].append(str({"type":"shapeless", "result_count": 1, "ingredients": [{"Count":9, "custom_data":f"{NAMESPACE}.{ore}"}]}))		
		pass
	
	# Ingredients (ingot, nugget, raw, and other)
	for ingredient in ingredients:
		item = ""
		if ingredient == "raw":
			item = f"raw_{ore}"
		elif ingredient == "":
			item = ore
		else:
			item = f"{ore}_{ingredient}"
		if f"{item}.png" not in textures_filenames: # Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		if any(item in texture for texture in textures_filenames):
			DATABASE[item] = {}
			DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA	# Item for ingredients
			DATABASE[item]["smithed"] = {}
			DATABASE[item]["smithed"]["dict"] = {ingredient: {ore: 1}}
			DATABASE[item]["smithed"]["ignore"] = {"functionality": 1, "crafting": 1}	# As it's a custom item, we don't want the CUSTOM_ITEM_VANILLA to be used
			DATABASE[item]["display"] = {}
			DATABASE[item]["display"]["Name"] = f'[{{"text":"{item_str}","italic":false,"color":"white"}}]'
			DATABASE[item]["display"]["Lore"] = [f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]']
		DATABASE[item][NAMESPACE] = {item:1}

		# Crafting
		DATABASE[item]["result_of_crafting"] = []
		if ingredient == "ingot" or ingredient == "":
			if f"{ore}_block.png" in textures_filenames:
				DATABASE[item]["result_of_crafting"].append(str({"type":"shapeless", "result_count": 9, "ingredients": [{"Count":1, "custom_data":f"{NAMESPACE}.{ore}_block"}]}))
			if f"{ore}_nugget.png" in textures_filenames:
				DATABASE[item]["result_of_crafting"].append(str({"type":"shapeless", "result_count": 1, "ingredients": [{"Count":9, "custom_data":f"{NAMESPACE}.{ore}_nugget"}]}))
		pass

	# Armors

	pass

# If no crafting, remove
for k in DATABASE.keys():
	if not DATABASE[k]["result_of_crafting"]:
		del DATABASE[k]["result_of_crafting"]


# Print not used textures and then all the keys
textures_filenames = [texture for texture in textures_filenames if not DATABASE.get(texture.replace(".png",""))]

for texture in textures_filenames:
	warning(f"Texture '{texture}' is not used in the database")
	pass
info("Database generated, here are the keys:\n" + ", ".join(DATABASE.keys()))

# Export database to JSON for debugging generation
with open(DATABASE_DEBUG, "w") as f:
	
	# Adjustments for better readability
	deep_copy = json.loads(json.dumps(DATABASE))	# Deep copy to avoid modifying the original database
	for k in deep_copy.keys():
		deep_copy[k]["smithed"] = str(deep_copy[k]["smithed"])
		deep_copy[k]["display"] = str(deep_copy[k]["display"])
		if deep_copy[k].get(NAMESPACE):
			deep_copy[k][NAMESPACE] = str(deep_copy[k][NAMESPACE])
	
	# Adjustments for better readability
	json.dump(deep_copy, f, indent = '\t')
	pass

