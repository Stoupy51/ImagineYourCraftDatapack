
# Import config
from src.importer import *

# Constants
MAX_ITEMS_PER_ROW = 5
MAX_ROWS_PER_PAGE = 5
MAX_ITEMS_PER_PAGE = MAX_ITEMS_PER_ROW * MAX_ROWS_PER_PAGE # (for showing up all items in the categories pages)

# Calculate left padding for categories pages depending on MAX_ITEMS_PER_ROW: higher the value, lower the padding
left_padding = 6 - MAX_ITEMS_PER_ROW

# Utils functions for fonts (item start at 0x0000, pages at 0xa000)
def get_font(i: int):
	""" Return the character that will be used for font, ex: "\u0002" with i = 2"""
	return f"\\u{i:04x}"
def get_page_font(i: int) -> str:
	return get_font(i + 0xa000)
def get_item_font(i: int) -> str:
	return get_font(i)

# Generate categories list
categories = {}
lowest_cmd = None
for item, data in DATABASE.items():
	cmd = data["custom_model_data"]
	if lowest_cmd is None or cmd < lowest_cmd:
		lowest_cmd = cmd

	if CATEGORY not in data:
		warning(f"Item '{item}' has no category key. Skipping.")
		continue

	category = data[CATEGORY]
	if category not in categories:
		categories[category] = []
	categories[category].append(item)

# Error message if there is too many categories
if len(categories) > MAX_ITEMS_PER_PAGE:
	error(f"Too many categories ({len(categories)}). Maximum is {MAX_ITEMS_PER_PAGE}. Please reduce the number of item categories.")

# Debug categories and sizes
s = ""
for category, items in categories.items():
	s += f"\n- {category}: {len(items)} items"
	if len(items) > MAX_ITEMS_PER_PAGE:
		s += f" (splitted into {len(items) // MAX_ITEMS_PER_PAGE + 1} pages)"
debug(f"Found {len(categories)} categories:{s}")

# Split up categories into pages
categories_pages = {}
for category, items in categories.items():
	i = 0
	while i < len(items):
		page_name = category.title()
		if len(items) > MAX_ITEMS_PER_PAGE:
			number = i // MAX_ITEMS_PER_PAGE + 1
			page_name += f" #{number}"
		new_items = items[i:i + MAX_ITEMS_PER_PAGE]
		categories_pages[page_name] = new_items
		i += MAX_ITEMS_PER_PAGE

# Prepare pages (append categories first, then items)
pages = []
i = 2 # Skip first two pages (introduction + categories)
for page_name, items in categories_pages.items():
	pages.append({"number": i, "name": page_name, "raw_data": items, "type": CATEGORY})
	i += 1
for item, data in DATABASE.items():
	if CATEGORY in data:
		pages.append({"number": i, "name": item, "raw_data": data, "type": "item"})
		i += 1

## TODO Prepare first two pages (introduction + link to categories)
first_page = {}
second_page = {}

"""
"minecraft:written_book_content": {
	"title": "Title",
	"author": "Author",
	"pages": [
		"[{\"text\":\"test\"}]",
		"[{\"text\":\"test\"}]"
	]
}"""

# Encode pages
for page in pages:
	content = []

	# Encode categories
	if page["type"] == CATEGORY:
		pass

	# Encode items
	else:

		# Get item data and page font depending on the custom model data
		name = page["name"]
		data = page["raw_data"]
		base_id = data["custom_model_data"] - lowest_cmd
		page_font = get_page_font(base_id)
		item_font = get_item_font(base_id)

		# If there are crafts
		if data.get(RESULT_OF_CRAFTING):
			first_craft = data[RESULT_OF_CRAFTING][0]

			"""
			item='{"text":"\\\\uef01","font":"simpledrawer:font","color":"white","hoverEvent":{"action":"show_item","contents":XXX},"clickEvent":{"action":"change_page","value":"YYY"}},'
			"""
			



