
# This python script tries generates a database of every block and item by using checking the textures folder
# It should be imported to fill the DATABASE variable
from src.importer import *
from database.additions import database_additions

# Get every item texture paths from textures folder
textures_filenames = [f for f in os.listdir(TEXTURES_FOLDER) if os.path.isfile(os.path.join(TEXTURES_FOLDER, f))]
textures_filenames = [f for f in textures_filenames if not any(s in f for s in SIDES)]	# Remove sides

# Generate ores things
others = ["stick", "rod"]
ores = ["adamantium", "emerald", "massive_obsidian", "ruby", "sapphire", "topaz", "steel", "lignite", "slate", "stone"]
placeables = ["block", "ore"]
ingredients = ["ingot", "nugget", "dust", "fragment", "raw", ""]
equipments = ["helmet", "chestplate", "leggings", "boots", "sword", "pickaxe", "axe", "shovel", "hoe"]
for ore in ores:
	material = ore.replace("massive_","")
	ingr = f"{material}_ingot" if f"{material}_ingot.png" in textures_filenames else ore	# Check if it's an ingot or no

	# Get ore color (for armor and other stuff)
	color = None
	if f"{ore}_block.png" in textures_filenames:
		with open(f"{TEXTURES_FOLDER}/{ore}_block.png", "rb") as file:
			color = imageio.imread(file).mean(axis = (0,1))	# Get average color (r,g,b,a)
			color = int(256*256*color[0] + 256*color[1] + color[2])	# Convert to int (Minecraft format: 256*256*red + 256*green + blue)

	# Placeables
	for placeable in placeables:
		block = f"{ore}_{placeable}"
		if f"{block}.png" not in textures_filenames:	# Skip if the block doesn't have a texture
			continue
		block_str = block.replace("_"," ").title()
		DATABASE[block] = {}
		DATABASE[block]["id"] = CUSTOM_BLOCK_VANILLA	# Item for placing custom block
		DATABASE[block]["smithed"] = {}
		DATABASE[block]["smithed"]["dict"] = {"block": {material: 1}}
		if placeable == "ore":
			DATABASE[block]["smithed"]["dict"]["ore"] = {material: 1}
		
		# Recipes
		DATABASE[block][CRAFTING_RECIPES] = []
		if placeable == "block":
			if f"{material}_ingot.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append(str({"type":"shapeless", "result_count": 1, "ingredients": [ingr_repr(f"{material}_ingot", count = 9)]}))
			if f"{material}_fragment.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append(str({"type":"shapeless", "result_count": 1, "ingredients": [ingr_repr(f"{material}_fragment", count = 9)]}))
			if f"{material}.png" in textures_filenames:
				DATABASE[block][CRAFTING_RECIPES].append(str({"type":"shapeless", "result_count": 1, "ingredients": [ingr_repr(material, count = 9)]}))
		pass
	
	# Ingredients (ingot, nugget, raw, and other)
	for ingredient in ingredients:
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
		DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA	# Item for ingredients
		DATABASE[item]["smithed"] = {}
		DATABASE[item]["smithed"]["dict"] = {ingredient: {material: 1}}

		# Recipes
		DATABASE[item][CRAFTING_RECIPES] = []
		if ingredient == "ingot" or ingredient == "":
			if f"{ore}_block.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append(str({"type":"shapeless", "result_count": 9, "ingredients": [ingr_repr(f"{ore}_block", count = 1)]}))
			if f"{ore}_nugget.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append(str({"type":"shapeless", "result_count": 1, "ingredients": [ingr_repr(f"{ore}_nugget", count = 9)]}))
			if f"raw_{ore}.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append(str({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"raw_{ore}")}))
			if f"{ore}_dust.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append(str({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"{ore}_dust")}))
			if f"{ore}_ore.png" in textures_filenames:
				DATABASE[item][CRAFTING_RECIPES].append(str({"type":"smelting", "result_count": 1, "ingredient": ingr_repr(f"{ore}_ore")}))
		pass

	# Armors and Tools
	for gear in equipments:
		item = f"{material}_{gear}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		armor_or_tools = "armor" if gear in equipments[:4] else "tools"
		DATABASE[item] = {}
		if armor_or_tools == "armor": # Is Armor?
			DATABASE[item]["id"] = f"minecraft:leather_{gear}"	# Leather armor by default
		else:
			DATABASE[item]["id"] = f"minecraft:diamond_{gear}"	# Diamond tools by default
		DATABASE[item]["smithed"] = {}
		DATABASE[item]["smithed"]["dict"] = {armor_or_tools: {material: 1, gear: 1}}
		craft_gear = None
		if gear == "helmet":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXXX X", "ingredients": {"X": ingr_repr(ingr)}}
		elif gear == "chestplate":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X XXXXXXX", "ingredients": {"X": ingr_repr(ingr)}}
		elif gear == "leggings":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXXX XX X", "ingredients": {"X": ingr_repr(ingr)}}
		elif gear == "boots":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X XX X", "ingredients": {"X": ingr_repr(ingr)}}
		elif gear == "sword":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X  X  S", "ingredients": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "pickaxe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XXX S  S ", "ingredients": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "axe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XX XS  S ", "ingredients": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "shovel":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "X  S  S  ", "ingredients": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		elif gear == "hoe":
			craft_gear = {"type": "shaped", "result_count": 1, "shape": "XX  S  S ", "ingredients": {"X": ingr_repr(ingr), "S": {"id":"minecraft:stick"}}}
		if craft_gear:
			DATABASE[item][CRAFTING_RECIPES] = [str(craft_gear)]

		# If armor, get color and put it in display
		if armor_or_tools == "armor" and color:
			if not DATABASE[item].get("display"):
				DATABASE[item]["display"] = {}
			DATABASE[item]["display"]["color"] = color
			

	# Others (stick, rod, ...)
	for misc in others:
		item = f"{material}_{misc}"
		if f"{item}.png" not in textures_filenames:	# Skip if the item doesn't have a texture
			continue
		item_str = item.replace("_"," ").title()
		DATABASE[item] = {}
		DATABASE[item]["id"] = CUSTOM_ITEM_VANILLA	# Item for ingredients
		DATABASE[item]["smithed"] = {}
		DATABASE[item]["smithed"]["dict"] = {misc: {material: 1}}
		if misc == "stick":
			DATABASE[item][CRAFTING_RECIPES] = [ str({"type":"shaped", "result_count": 2, "shape": "X  X  ", "ingredients": {"X": ingr_repr(ingr)}}) ]
		elif misc == "rod":
			DATABASE[item][CRAFTING_RECIPES] = [ str({"type":"shaped", "result_count": 1, "shape": "X  X  X  ", "ingredients": {"X": ingr_repr(ingr)}}) ]
		pass
	pass

# Apply database additions
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v

# For every key
for k in DATABASE.keys():

	# Remove craft if not
	if DATABASE[k].get(CRAFTING_RECIPES) == []:
		del DATABASE[k][CRAFTING_RECIPES]
	
	# Make display for every item
	item_str = k.replace("_"," ").title()
	if not DATABASE[k].get("display"):
		DATABASE[k]["display"] = {}
	if not DATABASE[k]["display"].get("Name"):
		DATABASE[k]["display"]["Name"] = f'[{{"text":"{item_str}","italic":false,"color":"white"}}]' 
	if not DATABASE[k]["display"].get("Lore"):
		DATABASE[k]["display"]["Lore"] = [SOURCE_LORE]
	else:
		DATABASE[k]["display"]["Lore"].append(SOURCE_LORE)
	if not DATABASE[k].get("custom_model_data"):
		DATABASE[k]["custom_model_data"] = "PREFIX_XXX"

	# Private custom_data for
	DATABASE[k][NAMESPACE] = {k:1}

	# Smithed ignore vanilla behaviours
	if not DATABASE[k].get("smithed"):
		DATABASE[k]["smithed"] = {}
	DATABASE[k]["smithed"]["ignore"] = {"functionality": 1, "crafting": 1}

# Print not used textures and then all the keys
textures_filenames = [texture for texture in textures_filenames if not DATABASE.get(texture.replace(".png",""))]

for texture in textures_filenames:
	path = f"{TEXTURES_FOLDER}/{texture}".replace(f"{ROOT}/","")
	warning(f"Texture '{path}' is not used in the database")
	pass
info("Database generated, here are the keys: " + ", ".join(shuffled(list(DATABASE.keys()))[:7]) + "...")

# Export database to JSON for debugging generation
with open(DATABASE_DEBUG, "w") as f:
	super_json_dump(DATABASE, f)
	pass

