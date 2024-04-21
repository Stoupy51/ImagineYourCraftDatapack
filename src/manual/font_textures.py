
# Import config
from src.importer import *

# Utils functions for fonts (item start at 0x0000, pages at 0xa000)
# Return the character that will be used for font, ex: "\u0002" with i = 2
def get_font(i: int):
	i += 0x0020	# Minecraft only allow starting this value
	if i > 0xffff:
		error(f"Font index {i} is too big. Maximum is 0xffff.")
	return f"\\u{i:04x}"
def get_page_font(i: int) -> str:
	return get_font(i + 0xa000)
def get_item_font(i: int) -> str:
	return get_font(i + 0x1000)

# Generate page font function (called in utils)
providers = []
FURNACES_RECIPES_TYPES = ("smelting", "blasting", "smoking", "campfire_cooking")
MANUAL_PATH = f"{BUILD_FOLDER}/manual"
def generate_page_font(name: str, page_font: str, craft: dict|None = None) -> None:
	""" Generate the page font image with the proper items
	"""
	pass


# TODO Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
for item in DATABASE:
	pass


