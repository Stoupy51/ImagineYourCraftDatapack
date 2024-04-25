
# Import config
from src.config import *

# Import OpenGL and PIL Images
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

# Load texture
texture_id = None
def load_textures(textures: list[Image.Image]):
	""" Load the textures in one single ID and return it
	Args:
		textures (list[Image.Image]): The list of textures to load
	Returns:
		int: The texture ID
	"""
	new_width = 0
	new_height = 0
	for texture in textures:
		new_width += texture.size[0]
		new_height += texture.size[1]
	
	# Make a new image with the size of all textures
	texture_data = Image.new("RGBA", (new_width, new_height), color = (0,0,0,0))
	x = 0
	y = 0
	for texture in textures:
		texture_data.paste(texture.transpose(Image.FLIP_TOP_BOTTOM), (x, y))
		x += texture.size[0]
		y += texture.size[1]
	texture_data = texture_data.tobytes("raw", "RGBA")

	# Generate texture ID
	texture_id = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texture_id)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, new_width, new_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
	return


display = (OPENGL_RESOLUTION, OPENGL_RESOLUTION)
window = None
TRANSPARENCY_COLOR_INT = (0, 254, 0, 255)
TRANSPARENCY_COLOR_FLOAT = (0, 254/255, 0, 0)
is_setup = False
def setup_opengl():
	# Init pygame
	pygame.init()
	global window, is_setup
	window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | NOFRAME)

	glEnable(GL_TEXTURE_2D) # Enable texturing
	glEnable(GL_BLEND)		# Enable blending (for transparency)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	# Set up isometric projection
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	scale = 1.75
	glOrtho(-scale, scale, -scale, scale, -scale, scale)
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()
	glRotatef(35.264, 1.0, 0.0, 0.0)
	glRotatef(45.0, 0.0, 1.0, 0.0)
	is_setup = True

# Function for rendering block
def render_block(front_texture: Image, side_texture: Image, top_texture: Image) -> None:
	""" Render a block with the given textures
	Args:
		front_texture (Image): The front texture
		side_texture (Image): The side texture
		top_texture (Image): The top texture
	"""
	if not is_setup:
		setup_opengl()
	load_textures([front_texture, side_texture, top_texture])

	glClearColor(*TRANSPARENCY_COLOR_FLOAT)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glBegin(GL_QUADS)

	# Front face
	vertices = ((-1,-1, 1), (1,-1, 1), (1, 1, 1), (-1, 1, 1))
	tex_coords = ((0, 0), (1/3, 0), (1/3, 1/3), (0, 1/3))
	for i in range(len(vertices)):
		glTexCoord2f(*tex_coords[i])
		glVertex3f(*vertices[i])

	# Top face
	vertices = ((-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1))
	tex_coords = ((1/3, 1/3), (2/3, 1/3), (2/3, 2/3), (1/3, 2/3))
	for i in range(len(vertices)):
		glTexCoord2f(*tex_coords[i])
		glVertex3f(*vertices[i])

	# Side face
	vertices = ((-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1))
	tex_coords = ((2/3, 2/3), (1, 2/3), (1, 1), (2/3, 1))
	for i in range(len(vertices)):
		glTexCoord2f(*tex_coords[i])
		glVertex3f(*vertices[i])
	
	# Update display
	glEnd()
	glDeleteTextures(texture_id)
	return

	

# Take a screenshot
def take_screenshot(save_path: str) -> None:
	""" Take a screenshot of the current window and save it
	Args:
		save_path (str): The path where to save the screenshot
	"""
	data = glReadPixels(0, 0, display[0], display[1], GL_RGBA, GL_UNSIGNED_BYTE)
	image = Image.frombytes("RGBA", display, data)
	image = image.transpose(Image.FLIP_TOP_BOTTOM)

	# Small crop
	x_crop = display[0] // 20
	y_crop = display[1] // 20
	image = image.crop((x_crop, y_crop, display[0] - x_crop, display[1] - y_crop))

	# Remove transparency + optimize image size
	pixels = image.load()
	width, height = image.size
	for x in range(width):
		for y in range(height):
			r, g, b, a = pixels[x, y]
			if a == 0 or (r, g, b, a) == TRANSPARENCY_COLOR_INT:
				pixels[x, y] = (0, 0, 0, 0)

	image.save(save_path, format = "PNG")
	pygame.display.flip()

# Stop OpenGL
def stop_opengl() -> None:
	""" Stop OpenGL and close the window """
	if is_setup:
		pygame.quit()

