
from src.config import *

# Constants
IGNORED_TEXTURES = ["world_icon","user_icon"]				# List of textures to ignore
IGNORED_TEXTURES = [t + ".png" for t in IGNORED_TEXTURES]	# Add .png to the list
STARTING_CMD = 2015000	# Prefix for custom_model_data

# Constants lists for defining items in link with ores
OTHERS = ["stick", "rod"]
ORES = ["adamantium", "emerald", "massive_obsidian", "ruby", "sapphire", "topaz", "steel", "lignite", "slate", "stone", "old_ruby"]
PLACEABLES = ["block", "ore"]
INGREDIENTS = ["ingot", "nugget", "dust", "fragment", "raw", ""]
EQUIPMENTS = ["helmet", "chestplate", "leggings", "boots", "sword", "pickaxe", "axe", "shovel", "hoe"]

# Get every item texture paths from textures folder
all_textures = [f for f in os.listdir(TEXTURES_FOLDER) if os.path.isfile(os.path.join(TEXTURES_FOLDER, f))]

# Remove sides and ignored textures
textures_filenames = [f for f in all_textures if (not any(s in f for s in SIDES) and f not in IGNORED_TEXTURES) or "topaz" in f]

