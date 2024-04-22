
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
def generate_page_font(name: str, page_font: str, craft: dict|None = None) -> None:
	""" Generate the page font image with the proper items
	"""
	pass

# TODO Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(path, exist_ok = True)
for item, data in DATABASE.items():
	
	# If it's not a block, simply copy the texture
	try:
		if data["id"] == CUSTOM_BLOCK_VANILLA:
			raise Exception()
		shutil.copy(f"{TEXTURES_FOLDER}/{item}.png", path)
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
			opengl.take_screenshot(f"{path}/{item}.png")			

		except Exception as e:
			warning(f"Failed to render iso for item {item}: {e}")

opengl.stop_opengl()

