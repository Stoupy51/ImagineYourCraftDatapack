
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
MANUAL_PATH = f"{ROOT}/manual"
def generate_page_font(name: str, page_font: str, craft: dict|None = None) -> None:
	""" Generate the page font image with the proper items
	"""
	pass


# Import OpenGL
import OpenGL.GL as gl
import glfw
glfw.init()

# Create a window
window = glfw.create_window(256, 256, "Isometric Render", None, None)
glfw.make_context_current(window)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

# TODO Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(path, exist_ok = True)
for item, data in DATABASE.items():
	
	# If it's not a block, simply copy the texture
	try:
		shutil.copy(f"{TEXTURES_FOLDER}/{item}.png", path)
	except:
			#continue
		# Else, render all the block textures and faces
#		try:
			# Load textures & Make front texture 50% darker and side_texture 25% darker
			front_texture = ImageEnhance.Brightness(Image.open(f"{TEXTURES_FOLDER}/{item}_front.png")).enhance(0.5)
			side_texture = ImageEnhance.Brightness(Image.open(f"{TEXTURES_FOLDER}/{item}_side.png")).enhance(0.75)
			top_texture = Image.open(f"{TEXTURES_FOLDER}/{item}_top.png")
			
			# Create the isometric render
			while not glfw.window_should_close(window):
				glfw.poll_events()
        
				gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
				gl.glLoadIdentity()
				
				# Set up the projection matrix and view matrix for isometric view
				gl.glMatrixMode(gl.GL_PROJECTION)
				gl.glLoadIdentity()
				gl.glMatrixMode(gl.GL_MODELVIEW)
				gl.glLoadIdentity()
				
				# Draw the block
				gl.glBegin(gl.GL_QUADS)
				gl.glColor3f(1, 1, 1)
				gl.glVertex3f(-1, -1, -1)
				gl.glVertex3f(1, -1, -1)
				gl.glVertex3f(1, 1, -1)
				gl.glVertex3f(-1, 1, -1)
				gl.glEnd()
				
				glfw.swap_buffers(window)
			


#		except Exception as e:
#			warning(f"Failed to render iso for item {item}: {e}")
			error("noob")


