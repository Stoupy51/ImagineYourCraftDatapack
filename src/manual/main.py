
# Import config
from src.importer import *
from src.manual.utils import *
from src.manual.book_optimizer import *

# Constants
MAX_ITEMS_PER_ROW = 5
MAX_ROWS_PER_PAGE = 5
MAX_ITEMS_PER_PAGE = MAX_ITEMS_PER_ROW * MAX_ROWS_PER_PAGE # (for showing up all items in the categories pages)

# Calculate left padding for categories pages depending on MAX_ITEMS_PER_ROW: higher the value, lower the padding
LEFT_PADDING = 6 - MAX_ITEMS_PER_ROW

# Copy assets in the resource pack
ASSETS_PATH = f"{ROOT}/src/manual/assets/"
if not DEBUG_MODE:
	super_copy(f"{ASSETS_PATH}/none_release.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/none.png")
else:
	super_copy(f"{ASSETS_PATH}/none.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/none.png")

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
	i += 1
	pages.append({"number": i, "name": page_name, "raw_data": items, "type": CATEGORY})
for item, data in DATABASE.items():
	if CATEGORY in data:
		i += 1
		pages.append({"number": i, "name": item, "raw_data": data, "type": "item"})

# Encode pages
book_content = []
os.makedirs(f"{FONT_FOLDER}/category", exist_ok=True)
simple_case = Image.open(f"{ASSETS_PATH}/simple_case_no_border.png")	# Load the simple case image for later use in categories pages
for page in pages:
	content = []
	number = page["number"]
	page_font = get_page_font(number)
	name = str(page["name"])
	raw_data = page["raw_data"]
	titled = name.replace("_", " ").title() + "\n"

	# TODO Encode categories {'number': 2, 'name': 'Material #1', 'raw_data': ['adamantium_block', 'adamantium_fragment', ...]}
	if page["type"] == CATEGORY:
		file_name = name.replace(" ", "_").replace("#", "").lower()
		providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/category/{file_name}.png", "ascent": 0, "height": 130, "chars": [page_font]})
		content.append({"text": "", "font": FONT, "color": "white"})	# Make default font for every next component
		content.append({"text": "➤ ", "font": "minecraft:default", "color": "black"})
		content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})
		content.append(SMALL_NONE_FONT + page_font + "\n")

		# Prepare image and line list
		page_image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
		x, y = 2, 2	# Prevision for global border and implicit border
		line = []

		# For each item in the category, get its page number and texture, then add it to the image
		for item in raw_data:
			item_data = DATABASE[item]
			texture_path = f"{MANUAL_PATH}/items/{NAMESPACE}/{item}.png"
			item_image = Image.open(texture_path)
			factor = 32 / item_image.size[0]
			item_image = item_image.resize((32, int(item_image.size[1] * factor)), Image.NEAREST)

			# Paste the simple case and the item_image
			page_image.paste(simple_case, (x, y))
			mask = item_image.convert("RGBA").split()[3]
			page_image.paste(item_image, (x + 2, y + 2), mask)
			x += 36

			# Add the clickEvent part to the line and add the 2 times the line if enough items
			line.append(get_item_component(item, ["custom_model_data", "custom_name"]))
			if len(line) == MAX_ITEMS_PER_ROW:
				line[-1]["text"] += "\n"
				line[0]["text"] = VERY_SMALL_NONE_FONT + line[0]["text"]
				content += line * 2
				line = []
				x = 2
				y += 36
		
		# If remaining items in the line, add them
		if len(line) > 0:
			line[-1]["text"] += "\n"
			line[0]["text"] = VERY_SMALL_NONE_FONT + line[0]["text"]
			content += line * 2
		
		# Add the border & Save the image
		page_image.save(f"{FONT_FOLDER}/category/{file_name}.png")

	# Encode items
	else:

		# If there are crafts
		if raw_data.get(RESULT_OF_CRAFTING):
			first_craft = raw_data[RESULT_OF_CRAFTING][0]
			l = generate_craft_content(first_craft, name, page_font)
			if l:
				content += l
		
		else:
			#providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{name}.png", "ascent": 0, "height": 60, "chars": [page_font]})
			content.append({"text": "", "font": FONT, "color": "white"})	# Make default font for every next component
			content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})

		# TODO: add wiki icons things

	# Add page to the book
	book_content.append(content)
book_content = optimize_book(book_content)


# Add fonts
providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 8, "height": 20, "chars": [NONE_FONT]})
providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 7, "height": 7, "chars": [SMALL_NONE_FONT]})
providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 0, "height": 2, "chars": [VERY_SMALL_NONE_FONT]})
fonts = {"providers": providers}
with super_open(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/font/manual.json", "w") as f:
	f.write(super_json_dump(fonts).replace("\\\\", "\\"))
		
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
			"pages": [str(i).replace("\\\\", "\\") for i in book_content]
		},
		"custom_model_data": lowest_cmd - 1
	}
}
DATABASE.update(manual_database)
info(f"Added manual to the database")

