
# Imports
from src.importer import *
from database.configurables import *

# Generate ores in database
for ore in ORES:
	material = ore.replace("massive_","")
	ingr = f"{material}_ingot" if f"{material}_ingot.png" in textures_filenames else ore	# Check if it's an ingot or no

	# Get ore color (for armor and other stuff)
	color = None
	if f"{ore}_block.png" in textures_filenames:
		with open(f"{TEXTURES_FOLDER}/{ore}_block.png", "rb") as file:
			color = imageio.imread(file).mean(axis = (0,1))	# Get average color (r,g,b,a)
			color = int(256*256*color[0] + 256*color[1] + color[2])	# Convert to int (Minecraft format: 256*256*red + 256*green + blue)

	# Placeables
	for placeable in PLACEABLES:
		block = f"{ore}_{placeable}"
		if f"{block}.png" not in textures_filenames:	# Skip if the block doesn't have a texture
			continue
		block_str = block.replace("_"," ").title()
		DATABASE[block] = {}
		DATABASE[block]["id"] = CUSTOM_BLOCK_VANILLA	# Item for placing custom block
		DATABASE[block]["custom_data"] = {"smithed":{}}	# Smithed convention
		DATABASE[block]["custom_data"]["smithed"]["dict"] = {"block": {material: 1}}
		if placeable == "ore":
			DATABASE[block]["custom_data"]["smithed"]["dict"]["ore"] = {material: 1}
		
		# Recipes
		DATABASE[block][CRAFTING_RECIPES] = []
		if placeable == "block":
			if f"{material}_ingot.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"shapeless", "result_count": 1, "INGREDIENTS": [ingr_repr(f"{material}_ingot", count = 9)]})
			if f"{material}_fragment.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"shapeless", "result_count": 1, "INGREDIENTS": [ingr_repr(f"{material}_fragment", count = 9)]})
			if f"{material}.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"shapeless", "result_count": 1, "INGREDIENTS": [ingr_repr(material, count = 9)]})
		pass
	
	# Ingredients (ingot, nugget, raw, and other)
	for ingredient in INGREDIENTS:
		if ingredient == "raw":
			item = f"raw_{material}"
		elif ingredient == "":
			item = material
		else:
			item = f"{material}_{ingredient}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		DATABASE[item] = {}
		DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA		# Item for INGREDIENTS
		DATABASE[item]["custom_data"] = {"smithed":{}}	# Smithed convention
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {ingredient: {material: 1}} if ingredient else {"material": {material: 1}}

		# Recipes
		DATABASE[item][CRAFTING_RECIPES] = []
		if ingredient == "ingot" or ingredient == "":
			if f"{ore}_block.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"shapeless", "result_count": 9, "INGREDIENTS": [ingr_repr(f"{ore}_block", count = 1)]})
			if f"{ore}_nugget.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"shapeless", "result_count": 1, "INGREDIENTS": [ingr_repr(f"{ore}_nugget", count = 9)]})
			if f"raw_{ore}.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"raw_{ore}")})
			if f"{ore}_dust.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"{ore}_dust")})
			if f"{ore}_ore.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"{ore}_ore")})
		pass

	# Armors and Tools
	for gear in EQUIPMENTS:
		item = f"{material}_{gear}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		armor_or_tools = "armor" if gear in EQUIPMENTS[:4] else "tools"
		DATABASE[item] = {}
		if armor_or_tools == "armor": # Is Armor?
			DATABASE[item]["id"] = f"minecraft:leather_{gear}"	# Leather armor by default
		else:
			DATABASE[item]["id"] = f"minecraft:diamond_{gear}"	# Diamond tools by default
		DATABASE[item]["custom_data"] = {"smithed":{}}			# Smithed convention
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {armor_or_tools: {material: 1, gear: 1}}
		craft_gear = None
		if gear == "helmet":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXXX X", "INGREDIENTS": {"X": ingr_repr(ingr)}}
		elif gear == "chestplate":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X XXXXXXX", "INGREDIENTS": {"X": ingr_repr(ingr)}}
		elif gear == "leggings":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXXX XX X", "INGREDIENTS": {"X": ingr_repr(ingr)}}
		elif gear == "boots":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X XX X", "INGREDIENTS": {"X": ingr_repr(ingr)}}
		elif gear == "sword":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X  X  S", "INGREDIENTS": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "pickaxe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXX S  S ", "INGREDIENTS": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "axe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XX XS  S ", "INGREDIENTS": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "shovel":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X  S  S  ", "INGREDIENTS": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "hoe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XX  S  S ", "INGREDIENTS": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		if craft_gear:
			DATABASE[item][CRAFTING_RECIPES] = [craft_gear]

		# If armor, get color and put it in display
		if armor_or_tools == "armor" and color:
			DATABASE[item]["dyed_color"] = color
			

	# Others (stick, rod, ...)
	for misc in OTHERS:
		item = f"{material}_{misc}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		DATABASE[item] = {}
		DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA		# Item for INGREDIENTS
		DATABASE[item]["custom_data"] = {"smithed":{}}	# Smithed convention
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {misc: {material: 1}}
		if misc == "stick":
			DATABASE[item][CRAFTING_RECIPES] = [{"type":"shaped", "result_count": 2, "shape": "X  X  ", "INGREDIENTS": {"X": ingr_repr(ingr)}}]
		elif misc == "rod":
			DATABASE[item][CRAFTING_RECIPES] = [{"type":"shaped", "result_count": 1, "shape": "X  X  X  ", "INGREDIENTS": {"X": ingr_repr(ingr)}}]
		pass
	pass
info("Ores related stuff generated in the database")

