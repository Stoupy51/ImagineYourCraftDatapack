
# Import config
from src.importer import *

# Utils functions for fonts (item start at 0x0000, pages at 0xa000)
# Return the character that will be used for font, ex: "\u0002" with i = 2
def get_font(i: int):
	return f"\\u{i:04x}"
def get_page_font(i: int) -> str:
	return get_font(i + 0xa000)
def get_item_font(i: int) -> str:
	return get_font(i)

"""
item_hover = '{"text":"\uef01","font":"simpledrawer:font","color":"white","hoverEvent":{"action":"show_item","contents":XXX},"clickEvent":{"action":"change_page","value":"YYY"}},'

craft = {"type": "crafting_shaped","result_count": 1,"category": "equipment","shape": ["XXX","X X"],"ingredients": {"X": {"components": {"custom_data": {"imagineyourcraft": {"adamantium": true}}}}}}

"""
# Generate all craft types content
def generate_craft_content(craft: dict, name: str, item_font: str) -> list:
	""" Generate the content for the craft type
	Args:
		craft		(dict):	The craft dictionary
		name		(str):	The name of the item, ex: "adamantium_pickaxe"
		item_font	(str):	The font for the item, ex: "\u0002"
	"""
	## TODO: all type (crafting_shaped, crafting_shapeless, ...)




