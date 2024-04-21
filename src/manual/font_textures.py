
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

import numpy as np
def rotation_matrix_3d(angle_x, angle_y, angle_z):
    """
    Create a 3D rotation matrix from the specified angles.
    
    :param angle_x: Rotation angle around the x-axis (in degrees)
    :param angle_y: Rotation angle around the y-axis (in degrees)
    :param angle_z: Rotation angle around the z-axis (in degrees)
    :return: 3x3 rotation matrix
    """
    # Convert angles to radians
    angle_x_rad = np.radians(angle_x)
    angle_y_rad = np.radians(angle_y)
    angle_z_rad = np.radians(angle_z)
    
    # Rotation matrices around each axis
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(angle_x_rad), -np.sin(angle_x_rad)],
                   [0, np.sin(angle_x_rad), np.cos(angle_x_rad)]])
    
    Ry = np.array([[np.cos(angle_y_rad), 0, np.sin(angle_y_rad)],
                   [0, 1, 0],
                   [-np.sin(angle_y_rad), 0, np.cos(angle_y_rad)]])
    
    Rz = np.array([[np.cos(angle_z_rad), -np.sin(angle_z_rad), 0],
                   [np.sin(angle_z_rad), np.cos(angle_z_rad), 0],
                   [0, 0, 1]])
    
    # Combine the rotation matrices
    rotation_matrix = Rz @ Ry @ Rx  # Apply rotations in the order: x, y, z
    
    return rotation_matrix


# TODO Generate iso renders for every item in the DATABASE
path = MANUAL_PATH + "/items"
os.makedirs(path, exist_ok = True)
for item, data in DATABASE.items():
	
	# If it's not a block, simply copy the texture
	try:
		shutil.copy(f"{TEXTURES_FOLDER}/{item}.png", path)
	except:
			continue
		# Else, render all the block textures and faces
#		try:
			# Load textures
			SCALING = 8
			working_size = (16*SCALING, 16*SCALING)
			front_texture = Image.open(f"{TEXTURES_FOLDER}/{item}_front.png")
			side_texture = Image.open(f"{TEXTURES_FOLDER}/{item}_side.png")
			top_texture = Image.open(f"{TEXTURES_FOLDER}/{item}_top.png")

			# Resize
			front_texture = front_texture.resize(working_size, Image.NEAREST)
			side_texture = side_texture.resize(working_size, Image.NEAREST)
			top_texture = top_texture.resize(working_size, Image.NEAREST)

			# Make front texture 50% darker and side_texture 25% darker
			front_texture = ImageEnhance.Brightness(front_texture).enhance(0.5)
			side_texture = ImageEnhance.Brightness(side_texture).enhance(0.75)

#		except Exception as e:
#			warning(f"Failed to render iso for item {item}: {e}")
			error("noob")


