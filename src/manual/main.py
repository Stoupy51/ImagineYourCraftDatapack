
# Import config
from src.importer import *
from src.manual.utils import *

# Constants
MAX_ITEMS_PER_ROW = 5
MAX_ROWS_PER_PAGE = 5
MAX_ITEMS_PER_PAGE = MAX_ITEMS_PER_ROW * MAX_ROWS_PER_PAGE # (for showing up all items in the categories pages)

# Calculate left padding for categories pages depending on MAX_ITEMS_PER_ROW: higher the value, lower the padding
left_padding = 6 - MAX_ITEMS_PER_ROW

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
i = 2 # Skip first two pages (introduction + categories)
for page_name, items in categories_pages.items():
	pages.append({"number": i, "name": page_name, "raw_data": items, "type": CATEGORY})
	i += 1
for item, data in DATABASE.items():
	if CATEGORY in data:
		pages.append({"number": i, "name": item, "raw_data": data, "type": "item"})
		i += 1

# Encode pages
book_content = []
for page in pages:

	# Encode categories
	if page["type"] == CATEGORY:
		pass

	# Encode items
	else:

		# Get item data and page font depending on the custom model data
		name = str(page["name"])
		data = page["raw_data"]
		base_id = data["custom_model_data"] - lowest_cmd
		page_font = get_page_font(base_id)
		item_font = get_item_font(base_id)

		# If there are crafts
		if data.get(RESULT_OF_CRAFTING):
			first_craft = data[RESULT_OF_CRAFTING][0]
			l = generate_craft_content(first_craft, name, page_font)
			if l:
				book_content.append(l)
		
		else:
			titled = name.replace("_", " ").title() + "\n"
			content = [{"text": "", "font": FONT, "color": "white"}]	# Make default font for every next component
			content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})
			book_content.append(content)


# Add fonts
providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 8, "height": 20, "chars": [NONE_FONT]})
providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 8, "height": 13, "chars": [SMALL_NONE_FONT*2]})
# providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/shaped_2x2.png", "ascent": 12, "height": 72, "chars": [SHAPED_2X2_FONT]})
# providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/shaped_3x3.png", "ascent": 0, "height": 60, "chars": [SHAPED_3X3_FONT]})
# providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/furnace.png", "ascent": 12, "height": 72, "chars": [FURNACE_FONT]})
fonts = {"providers": providers}
with super_open(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/font/manual.json", "w") as f:
	f.write(super_json_dump(fonts).replace("\\\\", "\\"))

# Copy assets in the resource pack
assets_path = f"{ROOT}/src/manual/assets/"
assets = os.listdir(assets_path)
if not DEBUG_MODE:
	assets.remove("none.png")
else:
	assets.remove("none_release.png")
os.makedirs(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font", exist_ok = True)
for file in assets:
	if file.endswith(".png"):
		if "none_release.png" == file and not DEBUG_MODE:
			shutil.copyfile(f"{assets_path}/none_release.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/none.png")
		else:
			shutil.copyfile(f"{assets_path}/{file}", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/{file}")

		
# Debug book_content
with super_open(f"{BUILD_RESOURCE_PACK}/debug_manual.json", "w") as f:
	f.write(super_json_dump(book_content).replace("\\\\", "\\"))
	debug(f"Debug book_content at '{BUILD_RESOURCE_PACK}/debug_manual.json'")

# Finally, prepend the manual to the database
manual_database = {"manual":
	{
		"id": "minecraft:written_book",
		"written_book_content": {
			"title": f"{DATAPACK_NAME} Manual",
			"author": AUTHOR,
			"pages": [str(i).replace("\\\\", "\\").replace(" ", "") for i in book_content]
		},
		"custom_model_data": lowest_cmd - 1
	}
}
DATABASE.update(manual_database)
info(f"Added manual to the database")

