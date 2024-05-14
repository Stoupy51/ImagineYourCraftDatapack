
# Import config & font textures
from config import *
from src.manual.font_textures import *
from src.utils.cache import simple_cache
MANUAL_ASSETS_PATH = f"{ROOT}/src/manual/assets/"

# Convert craft function
@simple_cache
def convert_shapeless_to_shaped(craft: dict) -> dict:
	""" Convert a shapeless craft to a shaped craft
	Args:
		craft (dict): The craft to convert
	Returns:
		dict: The craft converted
	"""
	new_craft = {"type": "crafting_shaped", "result_count": craft["result_count"], "ingredients": {}}
	if craft.get("result"):
		new_craft["result"] = craft["result"]

	# Get all ingredients to the dictionary
	next_key = "A"
	for ingr in craft["ingredients"]:
		key = next_key
		for new_key, new_ingr in new_craft["ingredients"].items():
			if str(ingr) == str(new_ingr):
				key = new_key
				break

		if key == next_key:
			new_craft["ingredients"][next_key] = ingr
			next_key = chr(ord(next_key) + 1)

	# Make the shape of the craft, with an exception when 2 materials to put one alone in the center
	if len(new_craft["ingredients"]) == 2 and len(craft["ingredients"]) == 9:
		new_craft["shape"] = ["AAA","ABA","AAA"]
	else:

		# For each ingredient, add to the shape depending on the occurences
		new_craft["shape"] = []
		for key, ingr in new_craft["ingredients"].items():
			for ingr_craft in craft["ingredients"]:
				if str(ingr_craft) == str(ingr):
					new_craft["shape"].append(key)
		
		# Fix the shape (ex: ["A","A","A","B","B","B","C","C","C"] -> ["AAA","BBB","CCC"])
		# ex 2: ["A","B","C","D"] -> ["AB","CD"]
		col_size = 3
		if len(new_craft["shape"]) <= 4:
			col_size = 2
		ranged = range(0, len(new_craft["shape"]), col_size)
		new_craft["shape"] = ["".join(new_craft["shape"][i:i + col_size]) for i in ranged]
	
	# Return the shaped craft
	return new_craft

# Get page number
pages = []	# Filled in src/manual/main.py
@simple_cache
def get_page_number(item_id: str) -> int:
	for p in pages:
		if p["name"] == item_id:
			return p["number"]
	return -1

# Convert ingredient to formatted JSON for book
COMPONENTS_TO_IGNORE = NOT_COMPONENTS + ["custom_data", "count"]
@simple_cache
def get_item_component(ingredient: dict|str, only_those_components: list[str] = None) -> dict:
	""" Generate item hover text for a craft ingredient
	Args:
		ingredient (dict|str): The ingredient
			ex: {'components': {'custom_data': {'iyc': {'adamantium_fragment': True}}}}
			ex: {'item': 'minecraft:stick'}
			ex: "adamantium_fragment"	# Only available for the datapack items
	Returns:
		dict: The text component
			ex: {"text":NONE_FONT,"color":"white","hoverEvent":{"action":"show_item","contents":{"id":"minecraft:command_block", "components": {...}}},"clickEvent":{"action":"change_page","value":"8"}}
			ex: {"text":NONE_FONT,"color":"white","hoverEvent":{"action":"show_item","contents":{"id":"minecraft:stick"}}}
	"""
	# Get the item id
	formatted = {"text": NONE_FONT, "hoverEvent":{"action":"show_item","contents":{"id":""}}}	# Default hoverEvent
	if isinstance(ingredient, dict) and ingredient.get("item"):
		formatted["hoverEvent"]["contents"]["id"] = ingredient["item"]
	else:
		# Get the item in the database
		if isinstance(ingredient, str):
			id = ingredient
			item = DATABASE[ingredient]
		else:
			custom_data = ingredient["components"]["custom_data"]
			id = ingr_to_id(ingredient, add_namespace = False)
			if custom_data.get(NAMESPACE):
				item = DATABASE.get(id)
			else:
				for data in custom_data.values():
					item = EXTERNAL_DATABASE.get(list(data.keys())[0])
					if item:
						break
		if not item:
			error("Item not found in database or external database: " + str(ingredient))
		
		# Copy id and components
		formatted["hoverEvent"]["contents"]["id"] = item["id"].replace("minecraft:", "")
		components = {}
		if only_those_components:
			for key in only_those_components:
				if key in item:
					components[key] = item[key]
		else:
			for key, value in item.items():
				if key not in COMPONENTS_TO_IGNORE:
					components[key] = value
		formatted["hoverEvent"]["contents"]["components"] = components

		# If item is from my datapack, get its page number
		page_number = get_page_number(id)
		if page_number != -1:
			formatted["clickEvent"] = {"action":"change_page","value":str(page_number)}
	
	# Return
	return formatted

# Constants
NONE_FONT = get_font(0x0000)
MEDIUM_NONE_FONT = get_font(0x0001)
SMALL_NONE_FONT = get_font(0x0002)
VERY_SMALL_NONE_FONT = get_font(0x0003)
WIKI_INFO_FONT = get_font(0x0004)
WIKI_RESULT_OF_CRAFT_FONT = get_font(0x0005)
WIKI_INGR_OF_CRAFT_FONT = get_font(0x0006)
FONT = f"{NAMESPACE}:manual"

# Generate all craft types content
def generate_craft_content(craft: dict, name: str, page_font: str) -> list:
	""" Generate the content for the craft type
	Args:
		craft		(dict):	The craft dictionary, ex: {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"adamantium": true}}}}}}
		name		(str):	The name of the item, ex: "adamantium_pickaxe"
		page_font	(str):	The font for the page, ex: "\u0002"
	Returns:
		list:	The content of the craft, ex: [{"text": ...}]
	"""
	craft_type = craft["type"]
	content = [{"text": "", "font": FONT, "color": "white"}]	# Make default font for every next component
	
	# Show up item title and page font
	titled = name.replace("_", " ").title() + "\n"
	content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})
	content.append(SMALL_NONE_FONT + page_font + "\n")

	# Convert shapeless crafting to shaped crafting
	if craft_type == "crafting_shapeless":
		craft = convert_shapeless_to_shaped(craft)
		craft_type = "crafting_shaped"
	
	# Generate the image for the page
	generate_page_font(name, page_font, craft)

	# Get result component
	result_component = get_item_component(name)
	if result_component.get("clickEvent"):
		del result_component["clickEvent"]	# Remove clickEvent for result item (as we already are on the page)

	# If the craft is shaped
	if craft_type == "crafting_shaped":

		# Convert each ingredients to its text component
		formatted_ingredients = {}
		for k, v in craft["ingredients"].items():
			formatted_ingredients[k] = get_item_component(v)

		# Add each ingredient to the craft
		for line in craft["shape"]:
			for _ in range(2):	# We need two lines to make a square, otherwise it will be a rectangle
				content.append(SMALL_NONE_FONT)
				for k in line:
					if k == " ":
						content.append(NONE_FONT)
					else:
						content.append(formatted_ingredients[k])
				content.append("\n")
		if len(craft["shape"]) == 1 and len(craft["shape"][0]) < 3:
			content.append("\n")
			pass
		
		# Add the result to the craft
		if len(craft["shape"]) <= 2 and len(craft["shape"][0]) <= 2:

			# First layer of the square
			len_1 = len(craft["shape"][0])
			offset_1 = 3 - len_1
			break_line_pos = content.index("\n", content.index("\n") + 1)	# Find the second line break
			content.insert(break_line_pos, NONE_FONT * offset_1)
			content.insert(break_line_pos + 1, result_component)
			
			# Second layer of the square
			len_2 = len(craft["shape"][1]) if len(craft["shape"]) > 1 else 0
			offset_2 = 3 - len_2
			if len_2 == 0:
				content.insert(break_line_pos + 2, "\n" + SMALL_NONE_FONT)
			break_line_pos = content.index("\n", break_line_pos + 3)	# Find the third line break
			content.insert(break_line_pos, NONE_FONT * offset_2)
			content.insert(break_line_pos + 1, result_component)
		else:
			# First layer of the square
			len_line = len(craft["shape"][1]) if len(craft["shape"]) > 1 else 0
			offset = 4 - len_line
			break_line_pos = content.index("\n", content.index("\n") + 1)	# Find the second line break
			try:
				break_line_pos = content.index("\n", break_line_pos + 1) # Find the third line break
			except:
				content.append(SMALL_NONE_FONT)
				break_line_pos = len(content)
			content.insert(break_line_pos, NONE_FONT * (offset - 1) + SMALL_NONE_FONT * 2)
			content.insert(break_line_pos + 1, result_component)

			# Second layer of the square
			try:
				break_line_pos = content.index("\n", break_line_pos + 3)	# Find the fourth line break
			except:
				content.append("\n" + SMALL_NONE_FONT)
				break_line_pos = len(content)
			content.insert(break_line_pos, NONE_FONT * (offset - 1) + SMALL_NONE_FONT * 2)
			content.insert(break_line_pos + 1, result_component)

			# Add break lines for the third layer of a 3x3 craft
			if len(craft["shape"]) < 3 and len(craft["shape"][0]) == 3:
				content.append("\n\n")
				if len(craft["shape"]) < 2:
					content.append("\n")
		
	
	# If the type is furnace type,
	elif craft_type in FURNACES_RECIPES_TYPES:
		
		# Convert ingredient to its text component
		formatted_ingredient = get_item_component(craft["ingredient"])

		# Add the ingredient to the craft
		for _ in range(2):
			content.append(SMALL_NONE_FONT)
			content.append(formatted_ingredient)
			content.append("\n")
		
		# Add the result to the craft
		for _ in range(2):
			content.append(SMALL_NONE_FONT * 4 + NONE_FONT * 2)
			content.append(result_component)
			content.append("\n")
		content.append("\n\n")

	return content

# Extract unique crafts from a craft list
def unique_crafts(crafts: list[dict]) -> list[dict]:
	""" Get unique crafts from a list of crafts
	Args:
		list (list[dict]): The list of crafts
	Returns:
		list[dict]: The unique crafts
	"""
	unique = []
	strings = []
	for craft in crafts:
		if str(craft) not in strings:
			unique.append(craft)
			strings.append(str(craft))
	return unique

# Generate USED_FOR_CRAFTING key like
def generate_otherside_crafts(item: str) -> list[dict]:
	""" Generate the USED_FOR_CRAFTING key like
	Args:
		item (str): The item to generate the key for
	Returns:
		list[dict]: ex: [{"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"chainmail": true}}}}},"result": {"item": "minecraft:chainmail_helmet","count": 1}}, ...]
	"""
	# Get all crafts that use the item
	crafts = []
	for key, value in DATABASE.items():
		if key != item and value.get(RESULT_OF_CRAFTING):
			for craft in value[RESULT_OF_CRAFTING]:
				if ("ingredient" in craft and item == ingr_to_id(craft["ingredient"], False)) or \
					("ingredients" in craft and isinstance(craft["ingredients"], dict) and item in [ingr_to_id(x, False) for x in craft["ingredients"].values()]) or \
					("ingredients" in craft and isinstance(craft["ingredients"], list) and item in [ingr_to_id(x, False) for x in craft["ingredients"]]):
					# Convert craft, ex:
					# before:	chainmail_helmet	{"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"chainmail": true}}}}}}}
					# after:	chainmail			{"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"chainmail": true}}}}},"result": {"item": "minecraft:chainmail_helmet","count": 1}}
					craft_copy = craft.copy()
					craft_copy["result"] = ingr_repr(key, craft["result_count"])
					crafts.append(craft_copy)
	return crafts


# Generate small craft icon
os.makedirs(f"{MANUAL_PATH}/font/wiki_icons", exist_ok = True)
@simple_cache
def generate_wiki_font_for_ingr(name: str, craft: dict) -> str:
	""" Generate the wiki icon font to display in the manual for wiki buttons showing the result of the craft
	If no texture found for the resulting item, return the default wiki font
	Args:
		name	(str):	The name of the item, ex: "adamantium_fragment"
		craft	(dict):	The associed craft, ex: {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"adamantium_fragment": true}}}}},"result": {"components": {"custom_data": {"iyc": {"adamantium_helmet": true}}},"count": 1}}
	Returns:
		str: The craft icon
	"""
	# Default wiki font
	font = WIKI_INGR_OF_CRAFT_FONT

	# If no result found, return the default font
	if not craft.get("result"):
		return font
	
	# Get result item texture and paste it on the wiki_ingredient_of_craft_template
	try:
		result_item = ingr_to_id(craft["result"]).replace(":", "/")
		texture_path = f"{MANUAL_PATH}/items/{result_item}.png"
		result_item = result_item.replace("/", "_")
		dest_path = f"{MANUAL_PATH}/font/wiki_icons/{result_item}.png"
		if not os.path.exists(dest_path):

			# Load texture and resize it
			item_texture = Image.open(texture_path)
			item_texture = item_texture.resize((42, 42), Image.NEAREST)
			item_texture = item_texture.convert("RGBA")

			# Load the template and paste the texture on it
			template = Image.open(f"{MANUAL_ASSETS_PATH}/wiki_ingredient_of_craft_template.png")
			template.paste(item_texture, (11, 11), item_texture)
			
			# Save the result
			template.save(dest_path)

		# Prepare provider
		font = get_next_font()
		providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/wiki_icons/{result_item}.png", "ascent": 8, "height": 16, "chars": [font]})

	except Exception as e:
		warning(f"Failed to generate craft icon for {name}: {e}\nreturning default font...")
		pass

	# Return the font
	return font

