
# Import config & font textures
from src.config import *
from src.manual.font_textures import *

# Convert craft function
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
def get_page_number(item_id: str) -> int:
	for p in pages:
		if p["name"] == item_id:
			return p["number"]
	return -1

# Convert ingredient to formatted JSON for book
COMPONENTS_TO_IGNORE = NOT_COMPONENTS + ["custom_data", "count"]
def get_item_component(ingredient: dict|str, only_those_components: list[str] = None) -> dict:
	""" Generate item hover text for a craft ingredient
	Args:
		ingredient (dict|str): The ingredient
			ex: {'components': {'custom_data': {'imagineyourcraft': {'adamantium_fragment': True}}}}
			ex: {'item': 'minecraft:stick'}
			ex: "adamantium_fragment"	# Only available for the datapack items
	Returns:
		dict: The text component
			ex: {"text":"\uef01","color":"white","hoverEvent":{"action":"show_item","contents":{"id":"minecraft:command_block", "components": {...}}},"clickEvent":{"action":"change_page","value":"8"}}
			ex: {"text":"\uef02","color":"white","hoverEvent":{"action":"show_item","contents":{"id":"minecraft:stick"}}}
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
			for key, value in item.items():
				if key in only_those_components:
					components[key] = value
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
		craft		(dict):	The craft dictionary, ex: {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"imagineyourcraft": {"adamantium": true}}}}}}
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

	# TODO: Add mouseEvent also for result item

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
	
	# If the type is furnace type,
	elif craft_type in FURNACES_RECIPES_TYPES:
		
		# Convert ingredient to its text component
		formatted_ingredient = get_item_component(craft["ingredient"])

		# Add the ingredient to the craft
		for _ in range(2):
			content.append(SMALL_NONE_FONT)
			content.append(formatted_ingredient)
			content.append("\n")

	return content


# Generate a border for a given Image
def add_border(image: Image.Image, border_color: tuple, border_size: int) -> Image.Image:
	""" Add a border to every part of the image
	Args:
		image			(Image):	The image to add the border
		border_color	(tuple):	The color of the border
		border_size		(int):		The size of the border
	Returns:
		Image: The image with the border
	"""
	# Convert image to RGBA
	image = image.copy().convert("RGBA")

	# Get the size of the image and load image
	width, height = image.size
	pixels = image.load()

	# For each pixel
	for x in range(width):
		for y in range(height):
			
			# If the pixel is transparent,
			if pixels[x, y][3] == 0:
				
				# Check if there is a pixel in a border_size*border_size range that is not transparent or equal to the border color
				found = False
				for dx in range(-border_size, border_size + 1):
					for dy in range(-border_size, border_size + 1):
						try:
							pixel = pixels[x + dx, y + dy]
							if pixel[3] != 0 and pixel != border_color:
								found = True
								break
						except IndexError:
							pass
					if found:
						break
				
				# If found, place the color
				if found:
					pixels[x, y] = border_color
	
	# Return the image
	return image


