
# Import config & font textures
from config import *
from src.manual.font_textures import *
from src.utils.cache import simple_cache

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
FONT = f"{NAMESPACE}:manual"

# Generate all craft types content
def generate_craft_content(craft: dict, name: str, page_font: str) -> list:
	""" Generate the content for the craft type
	Args:
		craft		(dict):	The craft dictionary, ex: {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"iyc": {"adamantium": true}}}}}}
		name		(str):	The name of the item, ex: "adamantium_pickaxe"
		page_font	(str):	The font for the page, ex: "\u0002"
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
		content.append("\n\n\n")

	return content


# Generate a border for a given Image
def add_border(image: Image.Image, border_color: tuple, border_size: int, is_rectangle_shape: bool) -> Image.Image:
	""" Add a border to every part of the image
	Args:
		image				(Image):	The image to add the border
		border_color		(tuple):	The color of the border
		border_size			(int):		The size of the border
		is_rectangle_shape	(bool):		If the shape is a rectangle or not (so we can choose between two algorithms)
	Returns:
		Image: The image with the border
	"""
	# Convert image to RGBA and load
	image = image.convert("RGBA")
	pixels = image.load()

	# Method 1: Image shape is not a rectangle
	if not is_rectangle_shape:
		# Get all transparent pixels
		pixels_to_change = [(x, y) for x in range(image.width) for y in range(image.height) if pixels[x, y][3] == 0]

		# Setup pixel view range (border_size * border_size)
		r = range(-border_size, border_size + 1)

		# For each pixel in the list, try to place border color
		for x, y in pixels_to_change:
			try:
				# If there is a pixel that is not transparent or equal to the border color in the range, place border_color
				if any(pixels[x + dx, y + dy][3] != 0 and pixels[x + dx, y + dy] != border_color for dx in r for dy in r):
					pixels[x, y] = border_color
			except:
				pass
	
	# Method 2: Image shape is a rectangle
	else:
		# Get image real height and width
		height, width = 8, 8
		while height < image.height and pixels[8, height][3]!= 0:
			height += 1
		while width < image.width and pixels[width, 8][3]!= 0:
			width += 1
		
		# Paste the border color in the image
		border = Image.new("RGBA", (width + 2, height + 2), border_color)
		border.paste(image, (0, 0), image)
		image.paste(border, (0, 0), border)
	
	# Return the image
	return image


