
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

# Generate page font function (called in utils)
providers = []
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
	print(name, page_font, craft["type"] if craft else "None")
	
	# Crafting shaped
	if craft and craft["type"] == "crafting_shaped":

		# Get the image template and append the provider
		shaped_size = max(2, max(len(craft["shape"]), len(craft["shape"][0])))
		template = Image.open(f"{TEMPLATES_PATH}/shaped_{shaped_size}x{shaped_size}.png")
		providers.append({"type":"bitmap","file":f"{NAMESPACE}:font/page/{name}.png", "ascent": 0, "height": 60, "chars": [page_font]})

		# Loop the shape matrix
		STARTING_PIXEL = (4, 4)
		SQUARE_SIZE = 32
		for i, row in enumerate(craft["shape"]):
			for j, symbol in enumerate(row):
				if symbol != " ":
					coords = (j*(SQUARE_SIZE + STARTING_PIXEL[0]), i*(SQUARE_SIZE + STARTING_PIXEL[1]))
					ingredient = craft["ingredients"][symbol]
					if ingredient.get("components"):
						# get "steel_ingot" in {'components': {'custom_data': {'imagineyourcraft': {'steel_ingot': True}}}}
						temp = ingredient["components"]["custom_data"]
						ns = list(temp.keys())[0]
						item = list(temp[ns].keys())[0]
						item = ns + ":" + item		# Custom item, ex: "imagineyourcraft:steel_ingot"
					else:
						item = ingredient["item"]	# Vanilla item, ex: "minecraft:glowstone"
					print(item)

		# Save the image
		template.save(f"{FONT_FOLDER}/page/{name}.png")
	
	return



# Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(path, exist_ok = True)
os.makedirs(f"{path}/{NAMESPACE}", exist_ok = True)
for item, data in DATABASE.items():
	
	# If it's not a block, simply copy the texture
	try:
		if data["id"] == CUSTOM_BLOCK_VANILLA:
			raise Exception()
		shutil.copy(f"{TEXTURES_FOLDER}/{NAMESPACE}/{item}.png", path)
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

		except Exception as e:
			warning(f"Failed to render iso for item {item}: {e}")

opengl.stop_opengl()

