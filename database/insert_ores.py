
# Imports
from src.importer import *
from database.configurables import *

# Generate ores in database
for ore in ORES:
	material = ore.replace("massive_","")
	ingr = f"{material}_ingot" if f"{material}_ingot.png" in textures_filenames else ore	# Check if it's an ingot or no
	# Get ingr repr
	if ingr in VANILLA_ITEMS:
		ingr = ingr_repr(f"minecraft:{ingr}")
	else:
		ingr = ingr_repr(ingr)

	# Get ore color (for armor and other stuff)
	color = None
	if f"{material}_chestplate.png" in textures_filenames:
		with open(f"{TEXTURES_FOLDER}/{material}_chestplate.png", "rb") as file:
			color = imageio.imread(file)										# Get image (2D Array)
			color = [(r,g,b) for dim in color for (r,g,b,a) in dim if a > 0]	# Get all colors that are not transparent
			color = [sum(x) / len(color) for x in zip(*color)]					# Get the average color
			color = int(color[0]) << 16 | int(color[1]) << 8 | int(color[2])	# Convert to int (Minecraft format: Red<<16 + Green<<8 + Blue)

	# Placeables
	for placeable in PLACEABLES:
		block = f"{ore}_{placeable}"
		if f"{block}.png" not in textures_filenames:	# Skip if the block doesn't have a texture
			continue
		block_str = block.replace("_"," ").title()
		DATABASE[block] = {}
		DATABASE[block]["id"] = CUSTOM_BLOCK_VANILLA	# Item for placing custom block
		DATABASE[block]["custom_data"] = {"smithed":{}}	# Smithed convention
		DATABASE[block]["custom_data"]["smithed"]["dict"] = {"block": {material: True}}
		if placeable == "ore":
			DATABASE[block]["custom_data"]["smithed"]["dict"]["ore"] = {material: True}
		
		# Recipes
		DATABASE[block][CRAFTING_RECIPES] = []
		if placeable == "block":
			if f"{material}_ingot.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"crafting_shaped","result_count":1,"group":material,"category":"misc","shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(f"{material}_ingot")}})
			if f"{material}_fragment.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"crafting_shaped","result_count":1,"group":material,"category":"misc","shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(f"{material}_fragment")}})
			if f"{material}.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append({"type":"crafting_shaped","result_count":1,"group":material,"category":"misc","shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(material)}})
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
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {ingredient: {material: True}} if ingredient else {"material": {material: True}}

		# Recipes
		DATABASE[item][CRAFTING_RECIPES] = []
		if ingredient == "ingot" or ingredient == "":
			if f"{ore}_block.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"crafting_shapeless","result_count":9,"category":"misc","group":material,"ingredients":[ingr_repr(f"{ore}_block")]})
			if f"{ore}_nugget.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"crafting_shaped","result_count":1,"category":"misc","group":material,"shape":["XXX","XXX","XXX"],"ingredients":{"X":ingr_repr(f"{ore}_nugget")}})
			if f"raw_{ore}.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"raw_{ore}")})
				DATABASE[item][CRAFTING_RECIPES].append({"type":"blasting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"raw_{ore}")})
			if f"{ore}_dust.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"{ore}_dust")})
				DATABASE[item][CRAFTING_RECIPES].append({"type":"blasting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"{ore}_dust")})
			if f"{ore}_ore.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append({"type":"smelting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":200,"ingredient":ingr_repr(f"{ore}_ore")})
				DATABASE[item][CRAFTING_RECIPES].append({"type":"blasting","result_count":1,"category":"misc","group":material,"experience":0.8,"cookingtime":100,"ingredient":ingr_repr(f"{ore}_ore")})
		pass

	# Armors and Tools
	for gear in EQUIPMENTS:
		item = f"{material}_{gear}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		armor_or_tools = "armor" if gear in ARMORS else "tools"
		DATABASE[item] = {}
		if armor_or_tools == "armor": # Is Armor?
			DATABASE[item]["id"] = f"minecraft:leather_{gear}"	# Leather armor by default
		else:
			DATABASE[item]["id"] = f"minecraft:diamond_{gear}"	# Diamond tools by default
		DATABASE[item]["custom_data"] = {"smithed":{}}			# Smithed convention
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {armor_or_tools: {material: True, gear: True}}
		craft_gear = None
		if gear == "helmet":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X"],"ingredients":{"X": ingr}}
		elif gear == "chestplate":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","XXX","XXX"],"ingredients":{"X": ingr}}
		elif gear == "leggings":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX","X X","X X"],"ingredients":{"X": ingr}}
		elif gear == "boots":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X X","X X"],"ingredients":{"X": ingr}}
		elif gear == "sword":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X  ","X  ","S  "],"ingredients":{"X": ingr,"S":ingr_repr("minecraft:stick")}}
		elif gear == "pickaxe":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XXX"," S "," S "],"ingredients":{"X": ingr,"S":ingr_repr("minecraft:stick")}}
		elif gear == "axe":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XX ","XS "," S "],"ingredients":{"X": ingr,"S":ingr_repr("minecraft:stick")}}
		elif gear == "shovel":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["X  ","S  ","S  "],"ingredients":{"X": ingr,"S":ingr_repr("minecraft:stick")}}
		elif gear == "hoe":
			craft_gear = {"type":"crafting_shaped","result_count":1,"category":"equipment","shape":["XX "," S "," S "],"ingredients":{"X": ingr,"S":ingr_repr("minecraft:stick")}}
		if craft_gear:
			DATABASE[item][CRAFTING_RECIPES] = [craft_gear]

		# If armor, get color and put it in display
		if armor_or_tools == "armor" and color:
			DATABASE[item]["dyed_color"] = {"rgb": color, "show_in_tooltip": False}
			

	# Others (stick, rod, ...)
	for misc in OTHERS:
		item = f"{material}_{misc}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		DATABASE[item] = {}
		DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA		# Item for INGREDIENTS
		DATABASE[item]["custom_data"] = {"smithed":{}}	# Smithed convention
		DATABASE[item]["custom_data"]["smithed"]["dict"] = {misc: {material: True}}
		if misc == "stick":
			DATABASE[item][CRAFTING_RECIPES] = [{"type":"crafting_shaped","result_count":2,"shape":["X  ","X  "],"ingredients":{"X":ingr}}]
		elif misc == "rod":
			DATABASE[item][CRAFTING_RECIPES] = [{"type":"crafting_shaped","result_count":1,"shape":["X  ","X  ","X  "],"ingredients":{"X":ingr}}]
		pass
	pass
info("Ores related stuff generated in the database")

