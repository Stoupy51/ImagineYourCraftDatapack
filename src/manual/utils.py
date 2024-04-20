
# Import config
from src.importer import *

# Utils functions for fonts (item start at 0x0000, pages at 0xa000)
# Return the character that will be used for font, ex: "\u0002" with i = 2
def get_font(i: int):
	i += 0x1000	# Minecraft only allow starting this value
	if i > 0xffff:
		error(f"Font index {i} is too big. Maximum is 0xffff.")
	return f"\\u{i:04x}"
def get_page_font(i: int) -> str:
	return get_font(i + 0xa000)
def get_item_font(i: int) -> str:
	return get_font(i + 0x1000)

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

"""
item_hover = '{"text":"\uef01","font":"simpledrawer:font","color":"white","hoverEvent":{"action":"show_item","contents":XXX},"clickEvent":{"action":"change_page","value":"YYY"}},'

"""

# Constants
FURNACES_RECIPES_TYPES = ("smelting", "blasting", "smoking", "campfire_cooking")
NONE_FONT = get_font(0x0000)
SMALL_NONE_FONT = get_font(0x0001)
SHAPED_1X1_FONT = get_font(0x0002)
SHAPED_2X2_FONT = get_font(0x0003)
SHAPED_3X3_FONT = get_font(0x0004)
FURNACE_FONT = get_font(0x0005)
FONT = f"{NAMESPACE}:manual"


# Generate all craft types content
def generate_craft_content(craft: dict, name: str, item_font: str) -> list:
	""" Generate the content for the craft type
	Args:
		craft		(dict):	The craft dictionary, ex: {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"imagineyourcraft": {"adamantium": true}}}}}}
		name		(str):	The name of the item, ex: "adamantium_pickaxe"
		item_font	(str):	The font for the item, ex: "\u0002"
	"""
	## TODO: all type (crafting_shaped, crafting_shapeless, ...)
	craft_type = craft["type"]
	content = []

	# Convert shapeless crafting to shaped crafting
	if craft_type == "crafting_shapeless":
		craft = convert_shapeless_to_shaped(craft)
		craft_type = "crafting_shaped"

	# If the craft is shaped
	if craft_type == "crafting_shaped":

		# Get the font to show up
		shape = SHAPED_1X1_FONT
		if len(craft["shape"][0]) == 2:
			shape = SHAPED_2X2_FONT
		if len(craft["shape"][0]) == 3:
			shape = SHAPED_3X3_FONT
		content.append({"text": shape, "font": FONT})

		# TODO: add the craft
		for _ in range(10):
			content.append({"text": NONE_FONT})
	
	# If the type is furnace type,
	elif craft_type in FURNACES_RECIPES_TYPES:
		pass

	return content




