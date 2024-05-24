
# Import config
from src.importer import *
from src.utils.io import *
from src.utils.print import *
from src.manual.utils import *
from src.manual.book_optimizer import *

# Constants
MAX_ITEMS_PER_PAGE = MAX_ITEMS_PER_ROW * MAX_ROWS_PER_PAGE # (for showing up all items in the categories pages)

# Calculate left padding for categories pages depending on MAX_ITEMS_PER_ROW: higher the value, lower the padding
LEFT_PADDING = 6 - MAX_ITEMS_PER_ROW

# Copy assets in the resource pack
if not DEBUG_MODE:
	super_copy(f"{MANUAL_ASSETS_PATH}/none_release.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/none.png")
else:
	super_copy(f"{MANUAL_ASSETS_PATH}/none.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/none.png")
super_copy(f"{MANUAL_ASSETS_PATH}/wiki_information.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/wiki_information.png")
super_copy(f"{MANUAL_ASSETS_PATH}/wiki_result_of_craft.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/wiki_result_of_craft.png")
super_copy(f"{MANUAL_ASSETS_PATH}/wiki_ingredient_of_craft.png", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/wiki_ingredient_of_craft.png")


# If the manual cache is enabled and we have a cache file, load it
if CACHE_MANUAL_PAGES and os.path.exists(MANUAL_DEBUG):
	with super_open(MANUAL_DEBUG, "r") as f:
		book_content = json.load(f)

# Else, generate all
else:

	# Generate categories list
	categories = {}
	for item, data in DATABASE.items():

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

	# Prepare pages (append categories first, then items depending on categories order
	i = 2 # Skip first two pages (introduction + categories)
	for page_name, items in categories_pages.items():
		i += 1
		pages.append({"number": i, "name": page_name, "raw_data": items, "type": CATEGORY})
	items_with_category = [(item, data) for item, data in DATABASE.items() if CATEGORY in data]
	category_list = list(categories.keys())
	sorted_database_on_category = sorted(items_with_category, key = lambda x: category_list.index(x[1][CATEGORY]))
	for item, data in sorted_database_on_category:
		i += 1
		pages.append({"number": i, "name": item, "raw_data": data, "type": "item"})

	# Encode pages
	book_content = []
	os.makedirs(f"{FONT_FOLDER}/category", exist_ok=True)
	simple_case = Image.open(f"{MANUAL_ASSETS_PATH}/simple_case_no_border.png")	# Load the simple case image for later use in categories pages
	for page in pages:
		content = []
		number = page["number"]
		page_font = get_page_font(number)
		name = str(page["name"])
		raw_data = page["raw_data"]
		titled = name.replace("_", " ").title() + "\n"

		# Encode categories {'number': 2, 'name': 'Material #1', 'raw_data': ['adamantium_block', 'adamantium_fragment', ...]}
		if page["type"] == CATEGORY:
			file_name = name.replace(" ", "_").replace("#", "").lower()
			providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/category/{file_name}.png", "ascent": 0, "height": 130, "chars": [page_font]})
			content.append({"text": "", "font": FONT, "color": "white"})	# Make default font for every next component
			content.append({"text": "➤ ", "font": "minecraft:default", "color": "black"})
			content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})
			content.append(SMALL_NONE_FONT * LEFT_PADDING + page_font + "\n")

			# Prepare image and line list
			page_image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
			x, y = 2, 2	# Prevision for global border and implicit border
			line = []

			# For each item in the category, get its page number and texture, then add it to the image
			for item in raw_data:
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
				component = get_item_component(item, ["custom_model_data", "item_name", "custom_name"])
				component["text"] = MEDIUM_NONE_FONT
				line.append(component)
				if len(line) == MAX_ITEMS_PER_ROW:
					line[-1]["text"] += "\n"
					line[0]["text"] = SMALL_NONE_FONT * LEFT_PADDING + line[0]["text"]
					content += line * 2
					line = []
					x = 2
					y += 36
			
			# If remaining items in the line, add them
			if len(line) > 0:
				line[-1]["text"] += "\n"
				line[0]["text"] = SMALL_NONE_FONT * LEFT_PADDING + line[0]["text"]
				content += line * 2
			
			# Add the 2 pixels border
			is_rectangle_shape = len(raw_data) % MAX_ITEMS_PER_ROW == 0
			page_image = add_border(page_image, BORDER_COLOR, BORDER_SIZE, is_rectangle_shape)
			
			# Save the image
			page_image.save(f"{FONT_FOLDER}/category/{file_name}.png")

		# Encode items
		else:

			# If there are crafts, generate the content for the first craft
			if raw_data.get(RESULT_OF_CRAFTING):
				first_craft = raw_data[RESULT_OF_CRAFTING][0]
				l = generate_craft_content(first_craft, name, page_font)
				if l:
					content += l
			
			# Else, generate the content for the single item in a big box
			else:
				generate_page_font(name, page_font, craft = None)
				component = get_item_component(name)
				component["text"] *= 2
				content.append({"text": "", "font": FONT, "color": "white"})	# Make default font for every next component
				content.append({"text": titled, "font": "minecraft:default", "color": "black", "underlined": True})
				content.append(MEDIUM_NONE_FONT * 2 + page_font + "\n")
				for _ in range(4):
					content.append(MEDIUM_NONE_FONT * 2)
					content.append(component)
					content.append("\n")

			## Add wiki information if any
			wiki_buttons = []
			if raw_data.get("wiki"):
				wiki_buttons.append({"text": WIKI_INFO_FONT + VERY_SMALL_NONE_FONT * 2, "hoverEvent": {"action": "show_text", "contents": raw_data["wiki"]}})
			
			# For each craft (except smelting dupes),
			crafts = []
			if raw_data.get(RESULT_OF_CRAFTING):
				crafts += raw_data[RESULT_OF_CRAFTING]
			if raw_data.get(USED_FOR_CRAFTING):
				crafts += raw_data[USED_FOR_CRAFTING]
			crafts += generate_otherside_crafts(name)
			crafts = [craft for craft in crafts if craft["type"] not in ["blasting", "smoking", "campfire_cooking"]]	# Remove smelting dupes
			crafts = unique_crafts(crafts)

			for i, craft in enumerate(crafts):
				if craft["type"] == "crafting_shapeless":
					craft = convert_shapeless_to_shaped(craft)
				craft_font = get_next_font()	# Unique used font for the craft
				generate_page_font(name, craft_font, craft, output_name = f"{name}_{i+1}")
				hover_text = [""]

				# Append the craft font and breaklines
				breaklines = 3
				if "shape" in craft:
					breaklines = max(2, max(len(craft["shape"]), len(craft["shape"][0])))
				hover_text.append({"text": craft_font + "\n\n" * breaklines, "font": FONT, "color": "white"})

				# Append ingredients
				if craft.get("ingredient"):
					id = ingr_to_id(craft["ingredient"], False).replace("_", " ").title()
					hover_text.append({"text": f"\n- x1 ", "color": "gray"})
					hover_text.append({"text": id, "color": "gray"})
				elif craft.get("ingredients"):

					# If it's a shaped crafting
					if isinstance(craft["ingredients"], dict):
						for k, v in craft["ingredients"].items():
							id = ingr_to_id(v, False).replace("_", " ").title()
							count = sum([line.count(k) for line in craft["shape"]])
							hover_text.append({"text": f"\n- x{count} ", "color": "gray"})
							hover_text.append({"text": id, "color": "gray"})
					
					# If it's shapeless
					elif isinstance(craft["ingredients"], list):
						ids = {}	# {id: count}
						for ingr in craft["ingredients"]:
							id = ingr_to_id(ingr, False).replace("_", " ").title()
							if id not in ids:
								ids[id] = 0
							ids[id] += 1
						for id, count in ids.items():
							hover_text.append({"text": f"\n- x{count} ", "color": "gray"})
							hover_text.append({"text": id, "color": "gray"})

				# Add the craft to the content
				result_or_ingredient = WIKI_RESULT_OF_CRAFT_FONT if "result" not in craft else generate_wiki_font_for_ingr(name, craft)
				wiki_buttons.append({"text": result_or_ingredient + VERY_SMALL_NONE_FONT * 2, "hoverEvent": {"action": "show_text", "contents": hover_text}})

				# If there is a result to the craft, try to add the clickEvent that change to that page
				if "result" in craft:
					result_item = ingr_to_id(craft["result"], False)
					if result_item in DATABASE:
						wiki_buttons[-1]["clickEvent"] = {"action": "change_page", "value": str(get_page_number(result_item))}
			
			# Add wiki buttons 5 by 5
			if wiki_buttons:

				# Add a breakline only if there aren't too many breaklines already
				content.append("\n")

				last_i = 0
				for i, button in enumerate(wiki_buttons):
					last_i = i
					# Duplicate line and add breakline
					if i % 5 == 0 and i != 0:
						# Remove VERY_SMALL_NONE_FONT from last button to prevent automatic break line
						content[-1]["text"] = content[-1]["text"].replace(VERY_SMALL_NONE_FONT, "")

						# Re-add last 5 buttons (for good hoverEvent) but we replace the wiki font by the small font
						content += ["\n"] + [x.copy() for x in content[-5:]]
						for j in range(5):
							content[-5 + j]["text"] = WIKI_NONE_FONT + VERY_SMALL_NONE_FONT * (2 if j != 4 else 0)
						content.append("\n")
					content.append(button)
				
				# Duplicate the last line if not done yet
				if last_i % 5 != 0 or last_i == 0:
					last_i = last_i % 5 + 1

					# Remove VERY_SMALL_NONE_FONT from last button to prevent automatic break line
					content[-1]["text"] = content[-1]["text"].replace(VERY_SMALL_NONE_FONT, "")

					content += ["\n"] + [x.copy() for x in content[-last_i:]]
					for j in range(last_i):
						content[-last_i + j]["text"] = WIKI_NONE_FONT + VERY_SMALL_NONE_FONT * (2 if j != 4 else 0)

		# Add page to the book
		book_content.append(content)

	## Add categories page
	content = []
	file_name = "categories_page"
	page_font = get_page_font(1)
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/category/{file_name}.png", "ascent": 0, "height": 130, "chars": [page_font]})
	content.append({"text": "", "font": FONT, "color": "white"})	# Make default font for every next component
	content.append({"text": "➤ ", "font": "minecraft:default", "color": "black"})
	content.append({"text": "Category browser\n", "font": "minecraft:default", "color": "black", "underlined": True})
	content.append(SMALL_NONE_FONT * LEFT_PADDING + page_font + "\n")

	# Prepare image and line list
	page_image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
	x, y = 2, 2	# Prevision for global border and implicit border
	line = []

	# For each item in the category, get its page number and texture, then add it to the image
	for page in pages:
		if page["type"] == CATEGORY:
			item = page["raw_data"][0]
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
			component = get_item_component(item, ["custom_model_data"])
			component["hoverEvent"]["contents"]["components"]["item_name"] = str({"text": page["name"], "color": "white"})
			component["clickEvent"]["value"] = str(page["number"])
			component["text"] = MEDIUM_NONE_FONT
			line.append(component)
			if len(line) == MAX_ITEMS_PER_ROW:
				line[-1]["text"] += "\n"
				line[0]["text"] = SMALL_NONE_FONT * LEFT_PADDING + line[0]["text"]
				content += line * 2
				line = []
				x = 2
				y += 36
	
	# If remaining items in the line, add them
	if len(line) > 0:
		line[-1]["text"] += "\n"
		line[0]["text"] = SMALL_NONE_FONT * LEFT_PADDING + line[0]["text"]
		content += line * 2
	
	# Add the 2 pixels border
	BORDER_COLOR = 0xB64E2F
	BORDER_SIZE = 2
	BORDER_COLOR = (BORDER_COLOR >> 16) & 0xFF, (BORDER_COLOR >> 8) & 0xFF, BORDER_COLOR & 0xFF, 255
	is_rectangle_shape = len(raw_data) % MAX_ITEMS_PER_ROW == 0
	page_image = add_border(page_image, BORDER_COLOR, BORDER_SIZE, is_rectangle_shape)
	
	# Save the image and add the page to the book
	page_image.save(f"{FONT_FOLDER}/category/{file_name}.png")
	book_content.insert(0, content)


	## Append introduction page
	content = [""]
	page_font = get_page_font(0)
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/_logo.png", "ascent": 0, "height": 40, "chars": [page_font]})
	content.append({"text": MANUAL_NAME + "\n", "underlined": True})
	content.append({"text": MEDIUM_NONE_FONT * 2 + page_font, "font": FONT, "color": "white"})
	
	# Create the image and load Minecraft font
	icon_path = f"{ASSETS_FOLDER}/original_icon.png"
	if not os.path.exists(icon_path):
		error(f"Missing icon path at '{icon_path}' (needed for the manual)")
	logo = Image.open(icon_path)
	logo = logo.resize((256, 256), Image.NEAREST)

	# Write the introduction text
	content.append("\n" * 6)
	content.append(MANUAL_FIRST_PAGE_TEXT)

	# Save image and insert in the manual pages
	logo.save(f"{FONT_FOLDER}/page/_logo.png")
	book_content.insert(0, content)

	## Optimize the book size
	book_content = optimize_book(book_content)

	# Add fonts
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 8, "height": 20, "chars": [NONE_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 8, "height": 18, "chars": [MEDIUM_NONE_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 7, "height": 7, "chars": [SMALL_NONE_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 0, "height": 2, "chars": [VERY_SMALL_NONE_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/none.png", "ascent": 7, "height": 16, "chars": [WIKI_NONE_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/wiki_information.png", "ascent": 8, "height": 16, "chars": [WIKI_INFO_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/wiki_result_of_craft.png", "ascent": 8, "height": 16, "chars": [WIKI_RESULT_OF_CRAFT_FONT]})
	providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/wiki_ingredient_of_craft.png", "ascent": 8, "height": 16, "chars": [WIKI_INGR_OF_CRAFT_FONT]})
	fonts = {"providers": providers}
	with super_open(f"{MANUAL_PATH}/font/manual.json", "w") as f:
		f.write(super_json_dump(fonts).replace("\\\\", "\\"))
			
	# Debug book_content
	with super_open(MANUAL_DEBUG, "w") as f:
		f.write(super_json_dump(book_content).replace("\\\\", "\\"))
		debug(f"Debug book_content at '{MANUAL_DEBUG}'")


# Copy the font provider and the generated textures to the resource pack
super_copy(f"{MANUAL_PATH}/font/manual.json", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/font/manual.json")
super_copy(f"{MANUAL_PATH}/font/category/", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/category/")
super_copy(f"{MANUAL_PATH}/font/page/", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/page/")
super_copy(f"{MANUAL_PATH}/font/wiki_icons/", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font/wiki_icons/")


# Finally, prepend the manual to the database
manual_database = {"manual":
	{
		"id": "minecraft:written_book",
		"written_book_content": {
			"title": MANUAL_NAME,
			"author": AUTHOR,
			"pages": [str(i).replace("\\\\", "\\") for i in book_content],
		},
		"lore": [json.dumps(SOURCE_LORE).replace('"', "'")],
		"custom_model_data": min(x["custom_model_data"] for x in DATABASE.values()) - 1,	# First custom_model_data minus 1
		"enchantment_glint_override": False,
	}
}
DATABASE.update(manual_database)
info(f"Added manual to the database")

