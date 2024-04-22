
# Import config
from src.importer import *

# Import OpenGL
import src.manual.opengl as opengl

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
SQUARE_SIZE = 32
FURNACES_RECIPES_TYPES = ("smelting", "blasting", "smoking", "campfire_cooking")
TEMPLATES_PATH = f"{ROOT}/src/manual/assets"
FONT_FOLDER = f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/textures/font"
os.makedirs(f"{FONT_FOLDER}/page", exist_ok=True)
def generate_page_font(name: str, page_font: str, craft: dict|None = None) -> None:
	""" Generate the page font image with the proper items
	Args:
		name (str): Name of the item
		page_font (str): Font string for the page
		craft (dict): Crafting recipe dictionary
	"""
	# Get result texture (to place later)
	result_texture = Image.open(f"{MANUAL_PATH}/items/{NAMESPACE}/{name}.png")
	
	# Crafting shaped
	if craft:
		factor = SQUARE_SIZE / result_texture.size[0]
		result_texture = result_texture.resize(
			(int(result_texture.size[0]*factor), int(result_texture.size[1]*factor)),
			Image.NEAREST
		)
		result_mask = result_texture.convert("RGBA").split()[3]

		if craft["type"] == "crafting_shaped":

			# Get the image template and append the provider
			shaped_size = max(2, max(len(craft["shape"]), len(craft["shape"][0])))
			template = Image.open(f"{TEMPLATES_PATH}/shaped_{shaped_size}x{shaped_size}.png")
			providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{name}.png", "ascent": 0, "height": 60, "chars": [page_font]})

			# Loop the shape matrix
			STARTING_PIXEL = (4, 4)
			CASE_OFFSETS = (4, 4)
			for i, row in enumerate(craft["shape"]):
				for j, symbol in enumerate(row):
					if symbol != " ":
						ingredient = craft["ingredients"][symbol]
						if ingredient.get("components"):
							# get "steel_ingot" in {'components': {'custom_data': {'imagineyourcraft': {'steel_ingot': True}}}}
							item = ingr_to_id(ingredient)
						else:
							item = ingredient["item"]	# Vanilla item, ex: "minecraft:glowstone"
						
						# Get the texture and place it at the coords
						item = item.replace(":", "/")
						item_texture = Image.open(f"{MANUAL_PATH}/items/{item}.png")
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
			template.save(f"{FONT_FOLDER}/page/{name}.png")
	
		elif craft and craft["type"] in FURNACES_RECIPES_TYPES:
			
			# Get the image template and append the provider
			template = Image.open(f"{TEMPLATES_PATH}/furnace.png")
			providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{name}.png", "ascent": 0, "height": 60, "chars": [page_font]})

			# Place input item
			input_item = ingr_to_id(craft["ingredient"])
			input_item = input_item.replace(":", "/")
			item_texture = Image.open(f"{MANUAL_PATH}/items/{input_item}.png")
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
			template.save(f"{FONT_FOLDER}/page/{name}.png")
	
	# Else, there is no craft, just put the item in a box
	else:
		# TODO
		pass

	
	return



# Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(f"{path}/{NAMESPACE}", exist_ok = True)
for item, data in DATABASE.items():
	# Skip if item is already generated
	if os.path.exists(f"{path}/{NAMESPACE}/{item}.png"):
		continue
	
	# If it's not a block, simply copy the texture
	try:
		if data["id"] == CUSTOM_BLOCK_VANILLA:
			raise Exception()
		super_copy(f"{TEXTURES_FOLDER}/{item}.png", f"{path}/{NAMESPACE}/{item}.png")
	except:
		# Else, render all the block textures and faces
		try:

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



## Copy every used vanilla items
# Get every used vanilla items
used_vanilla_items = set()
for item, data in DATABASE.items():
	if data.get(RESULT_OF_CRAFTING):
		for recipe in data[RESULT_OF_CRAFTING]:
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
	pass

# Download all the vanilla textures from the wiki
wiki_link = "https://minecraft.wiki/images/Invicon_ITEM.png"
for item in used_vanilla_items:
	destination = f"{path}/minecraft/{item}.png"
	if not os.path.exists(destination):
		response = requests.get(wiki_link.replace("ITEM", item.title()))
		if response.status_code != 200:
			# If the item is type of "X_block", try to get "block_of_X" texture instead
			if item.endswith("_block"):
				x = "_".join(item.split("_")[:-1])
				get = f"block_of_{x}".title().replace("_Of_","_of_")
				response = requests.get(wiki_link.replace("ITEM", get))
			if response.status_code != 200:
				error(f"Failed to download texture for item '{item}', please add it manually in '{path}/minecraft'")
				continue
		with super_open(destination, "wb") as file:
			file.write(response.content)
	pass

