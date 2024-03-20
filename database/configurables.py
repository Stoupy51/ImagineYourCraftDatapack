
from src.config import *

# Constants
IGNORED_TEXTURES = ["world_icon","user_icon"]	# List of textures to ignore
CMD_PREFIX = 2015	# Prefix for custom_model_data

# Constants lists for defining items in link with ores
OTHERS = ["stick", "rod"]
ORES = ["adamantium", "emerald", "massive_obsidian", "ruby", "sapphire", "topaz", "steel", "lignite", "slate", "stone"]
PLACEABLES = ["block", "ore"]
INGREDIENTS = ["ingot", "nugget", "dust", "fragment", "raw", ""]
EQUIPMENTS = ["helmet", "chestplate", "leggings", "boots", "sword", "pickaxe", "axe", "shovel", "hoe"]

# Get every item texture paths from textures folder
textures_filenames = [f for f in os.listdir(TEXTURES_FOLDER) if os.path.isfile(os.path.join(TEXTURES_FOLDER, f))]
textures_filenames = [f for f in textures_filenames if not any(s in f for s in SIDES)]	# Remove sides
textures_filenames = [f for f in textures_filenames if f not in IGNORED_TEXTURES]	# Remove ignored textures

