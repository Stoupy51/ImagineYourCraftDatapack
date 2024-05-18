
# Import config
from config import *
from src.utils.ingredients import *
from src.utils.print import *
from src.utils.io import *

# Imports
import src.manual.opengl as opengl
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import requests

# Constants
SQUARE_SIZE = 32
TEMPLATES_PATH = f"{ROOT}/src/manual/assets"
FONT_FOLDER = f"{MANUAL_PATH}/font"
BORDER_COLOR = 0xB64E2F
BORDER_SIZE = 2
BORDER_COLOR = (BORDER_COLOR >> 16) & 0xFF, (BORDER_COLOR >> 8) & 0xFF, BORDER_COLOR & 0xFF, 255


# Utils functions for fonts (item start at 0x0000, pages at 0xa000)
# Return the character that will be used for font, ex: "\u0002" with i = 2
def get_font(i: int):
	i += 0x0020	# Minecraft only allow starting this value
	if i > 0xffff:
		error(f"Font index {i} is too big. Maximum is 0xffff.")
	return f"\\u{i:04x}"
def get_page_font(i: int) -> str:
	return get_font(i + 0x1000)
next_craft_font = 0x8000
def get_next_font() -> str:	# Returns an incrementing value for each craft
	global next_craft_font
	next_craft_font += 1
	return get_font(next_craft_font)

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

# Generate an image showing the result count
def image_count(count: int) -> Image:
	""" Generate an image showing the result count
	Args:
		count (int): The count to show
	Returns:
		Image: The image with the count
	"""
	# Create the image
	img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(f"{ROOT}/src/manual/assets/minecraft_font.ttf", size = 16)

	# Calculate text size and positions of the two texts
	text_width, text_height = draw.textsize(str(count), font = font)
	pos_1 = (32-text_width), (32-text_height)
	pos_2 = (30-text_width), (30-text_height)
	
	# Draw the count
	draw.text(pos_1, str(count), (50, 50, 50), font = font)
	draw.text(pos_2, str(count), (255, 255, 255), font = font)
	return img

# Generate page font function (called in utils)
providers = []
os.makedirs(f"{FONT_FOLDER}/page", exist_ok=True)
def generate_page_font(name: str, page_font: str, craft: dict|None = None, output_name: str = "") -> None:
	""" Generate the page font image with the proper items
	Args:
		name			(str):			Name of the item
		page_font		(str):			Font string for the page
		craft			(dict|None):	Crafting recipe dictionary (None if no craft)
		output_name		(str|None):		The output name (None if default, used for wiki crafts)
	"""
	if not output_name:
		output_filename = name
	else:
		output_filename = output_name

	# Get result texture (to place later)
	image_path = f"{MANUAL_PATH}/items/{NAMESPACE}/{name}.png"
	if not os.path.exists(image_path):
		error(f"Missing item texture at '{image_path}'")
	result_texture = Image.open(image_path)

	# If recipe result is specified, take the right texture
	if craft and craft.get("result"):
		result_id = ingr_to_id(craft["result"])
		result_id = result_id.replace(":", "/")
		image_path = f"{MANUAL_PATH}/items/{result_id}.png"
		result_texture = Image.open(image_path)

	# Resize the texture and get the mask
	factor = SQUARE_SIZE / result_texture.size[0]
	result_texture = result_texture.resize(
		(int(result_texture.size[0]*factor), int(result_texture.size[1]*factor)),
		Image.NEAREST
	)
	result_mask = result_texture.convert("RGBA").split()[3]
	
	# Check if there is a craft
	if craft:

		# Shaped craft
		if craft["type"] in "crafting_shaped":

			# Get the image template and append the provider
			shaped_size = max(2, max(len(craft["shape"]), len(craft["shape"][0])))
			template = Image.open(f"{TEMPLATES_PATH}/shaped_{shaped_size}x{shaped_size}.png")
			providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{output_filename}.png", "ascent": 0 if not output_name else 6, "height": 60, "chars": [page_font]})

			# Loop the shape matrix
			STARTING_PIXEL = (4, 4)
			CASE_OFFSETS = (4, 4)
			for i, row in enumerate(craft["shape"]):
				for j, symbol in enumerate(row):
					if symbol != " ":
						ingredient = craft["ingredients"][symbol]
						if ingredient.get("components"):
							# get "iyc:steel_ingot" in {'components': {'custom_data': {'iyc': {'steel_ingot': True}}}}
							item = ingr_to_id(ingredient)
						else:
							item = ingredient["item"]	# Vanilla item, ex: "minecraft:glowstone"
						
						# Get the texture and place it at the coords
						item = item.replace(":", "/")
						image_path = f"{MANUAL_PATH}/items/{item}.png"
						if not os.path.exists(image_path):
							error(f"Missing item texture at '{image_path}'")
						item_texture = Image.open(image_path)
						factor = SQUARE_SIZE / item_texture.size[0]
						item_texture = item_texture.resize(
							(int(item_texture.size[0]*factor), int(item_texture.size[1]*factor)),
							Image.NEAREST
						)
						coords = (
							j * (SQUARE_SIZE + CASE_OFFSETS[0]) + STARTING_PIXEL[0],
							i * (SQUARE_SIZE + CASE_OFFSETS[1]) + STARTING_PIXEL[1]
						)
						mask = item_texture.convert("RGBA").split()[3]
						template.paste(item_texture, coords, mask)
			
			# Place the result item
			coords = (148, 40) if shaped_size == 3 else (118, 25)
			template.paste(result_texture, coords, result_mask)

			# Place count if the result is greater than 1
			if craft["result_count"] > 1:
				count_img = image_count(craft["result_count"])
				template.paste(count_img, [x + 2 for x in coords], count_img)

			# Save the image
			template.save(f"{FONT_FOLDER}/page/{output_filename}.png")

		# Smelting craft
		elif craft["type"] in FURNACES_RECIPES_TYPES:
			
			# Get the image template and append the provider
			template = Image.open(f"{TEMPLATES_PATH}/furnace.png")
			providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{output_filename}.png", "ascent": 0 if not output_name else 6, "height": 60, "chars": [page_font]})

			# Place input item
			input_item = ingr_to_id(craft["ingredient"])
			input_item = input_item.replace(":", "/")
			image_path = f"{MANUAL_PATH}/items/{input_item}.png"
			if not os.path.exists(image_path):
				error(f"Missing item texture at '{image_path}'")
			item_texture = Image.open(image_path)
			factor = SQUARE_SIZE / item_texture.size[0]
			item_texture = item_texture.resize(
				(int(item_texture.size[0]*factor), int(item_texture.size[1]*factor)),
				Image.NEAREST
			)
			mask = item_texture.convert("RGBA").split()[3]
			template.paste(item_texture, (4, 4), mask)

			# Place the result item and count if the result is greater than 1
			coords = (124, 40)
			template.paste(result_texture, coords, result_mask)
			if craft["result_count"] > 1:
				count_img = image_count(craft["result_count"])
				template.paste(count_img, [x + 2 for x in coords], count_img)
			
			# Save the image
			template.save(f"{FONT_FOLDER}/page/{output_filename}.png")
	
	# Else, there is no craft, just put the item in a box
	else:
		# Get the image template and append the provider
		template = Image.open(f"{TEMPLATES_PATH}/simple_case_no_border.png")
		providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{output_filename}.png", "ascent": 0 if not output_name else 6, "height": 40, "chars": [page_font]})

		# Place the result item
		template.paste(result_texture, (2, 2), result_mask)
		template = add_border(template, BORDER_COLOR, BORDER_SIZE, is_rectangle_shape = True)
		template.save(f"{FONT_FOLDER}/page/{output_filename}.png")
	return



# Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(f"{path}/{NAMESPACE}", exist_ok = True)
for item, data in DATABASE.items():
	
	# If it's not a block, simply copy the texture
	try:
		if data["id"] == CUSTOM_BLOCK_VANILLA:
			raise Exception()
		if not os.path.exists(f"{path}/{NAMESPACE}/{item}.png") or not CACHE_MANUAL_ASSETS:
			super_copy(f"{TEXTURES_FOLDER}/{item}.png", f"{path}/{NAMESPACE}/{item}.png")
	except:
		# Else, render all the block textures and faces
		try:
			# Skip if item is already generated (to prevent launcher OpenGL for nothing)
			if os.path.exists(f"{path}/{NAMESPACE}/{item}.png") and CACHE_MANUAL_ASSETS:
				continue

			# Load front texture
			sides = ("_front", "_side", "_top", "_bottom", "")
			front_path = f"{TEXTURES_FOLDER}/{item}"
			for side in sides:
				if os.path.exists(f"{front_path}{side}.png"):
					front_path += side
					break
			front_texture = Image.open(front_path + ".png")
			side_texture = front_texture
			top_texture = front_texture

			# Try to load side
			side_path = f"{TEXTURES_FOLDER}/{item}_side.png"
			if os.path.exists(side_path):
				side_texture = Image.open(side_path)
			
			# Try to load top texture
			top_path = f"{TEXTURES_FOLDER}/{item}_top.png"
			if os.path.exists(top_path):
				top_texture = Image.open(top_path)
			
			# Make front texture 50% darker and side texture 25% darker
			front_texture = ImageEnhance.Brightness(front_texture).enhance(0.5)
			side_texture = ImageEnhance.Brightness(side_texture).enhance(0.75)

			# Render block and take a screenshot
			opengl.render_block(front_texture, side_texture, top_texture)
			opengl.take_screenshot(f"{path}/{NAMESPACE}/{item}.png")

		except:
			try:
				super_copy(f"{TEXTURES_FOLDER}/{item}.png", f"{path}/{NAMESPACE}/{item}.png")
			except:
				error(f"Failed to render iso for item '{item}', please add it manually to '{path}/{NAMESPACE}/{item}.png'")
opengl.stop_opengl()
debug("Generated iso renders for all items, or used cached renders")


## Copy every used vanilla items
# Get every used vanilla items
used_vanilla_items = set()
for item, data in DATABASE.items():
	all_crafts = []
	if data.get(RESULT_OF_CRAFTING):
		all_crafts += data[RESULT_OF_CRAFTING]
	if data.get(USED_FOR_CRAFTING):
		all_crafts += data[USED_FOR_CRAFTING]
	for recipe in all_crafts:
		ingredients = []
		if "ingredients" in recipe:
			ingredients = recipe["ingredients"]
			if isinstance(ingredients, dict):
				ingredients = ingredients.values()
		elif "ingredient" in recipe:
			ingredients = [recipe["ingredient"]]
		for ingredient in ingredients:
			if "item" in ingredient:
				used_vanilla_items.add(ingredient["item"].split(":")[1])
		if "result" in recipe and "item" in recipe["result"]:
			used_vanilla_items.add(recipe["result"]["item"].split(":")[1])
	pass

# Download all the vanilla textures from the wiki
download_link = "https://raw.githubusercontent.com/edayot/renders/renders/resourcepack/assets/minecraft/textures/render/"
for item in used_vanilla_items:
	destination = f"{path}/minecraft/{item}.png"
	if not (os.path.exists(destination) and CACHE_MANUAL_ASSETS):	# If not downloaded yet or not using cache
		debug(f"Downloading texture for item '{item}'...")
		response = requests.get(f"{download_link}item/{item}.png")
		if response.status_code == 200:
			with super_open(destination, "wb") as file:
				file.write(response.content)
			debug(f"Downloaded texture for item '{item}'!")
		else:
			warning(f"Failed to download texture for item '{item}', please add it manually to '{destination}'")
			warning(f"Suggestion link: '{download_link}'")
	pass
debug("Downloaded all the vanilla textures, or using cached ones")

