
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
		
		# Crafting block into 9x ingot
		if placeable == "block" and any(f"{ore}_ingot" in texture for texture in textures_filenames):
			DATABASE[block]["crafting"] = [
				str({"type":"shapeless", "result_count": 9, "ingredients": [{"Count":1,"custom_data":f"{NAMESPACE}.{block}"}]}),
			]
		pass
	
	# Ingredients (ingot, nugget, raw, and other)
	if ore != "massive_obsidian":
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
			DATABASE[item]["crafting"] = []

			# If no crafting, remove
			if not DATABASE[item]["crafting"]:
				del DATABASE[item]["crafting"]
		pass

	# Armors





# Print not used textures and then all the keys
for k in DATABASE.keys():
	if k in textures_filenames:
		textures_filenames.remove(k)
		pass
	pass
for texture in textures_filenames:
	warning(f"Texture '{texture}' is not used in the database")
	pass
info("Database generated, here are the keys:\n" + ", ".join(DATABASE.keys()))

# Adjustments
for k in DATABASE.keys():
	DATABASE[k]["smithed"] = str(DATABASE[k]["smithed"])
	DATABASE[k]["display"] = str(DATABASE[k]["display"])
	if DATABASE[k].get(NAMESPACE):
		DATABASE[k][NAMESPACE] = str(DATABASE[k][NAMESPACE])


# Export database to JSON for debugging generation (TO COMMENT WHEN NOT DEBUGGING)
with open("database_debug.json", "w") as f:
	json.dump(DATABASE, f, indent = '\t')
	pass

