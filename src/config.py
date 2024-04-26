
# Imports
import os

# Datapack related constants
DEBUG_MODE = False		# Shows up grids in manual
CACHE_MODE = True		# Caches the minecraft assets and the items renders for the manual (manual/items/*.png)
MINECRAFT_VERSION = "1.20.5 pre-release 1"
VERSION = "0.0.1"
NAMESPACE = "imagineyourcraft"
GLOBAL_NAMESPACE = "stoupy"
PACK_FORMAT = 41
RESOURCE_PACK_FORMAT = 32
DATA_VERSION = 3835
DEPENDENCIES = {
	"common_signals": {"version":[0, 0, 0], "name":"Common Signals", "url":"https://github.com/Stoupy51/CommonSignals"},
	# "smithed.custom_block": {"version":[0, 0, 0], "name":"Smithed Custom Block Placement", "url":"https://wiki.smithed.dev/libraries/custom-block/"},
	# "smithed.crafter": {"version":[0, 0, 0], "name":"Smithed Crafter", "url":"https://wiki.smithed.dev/libraries/crafter/"},
	# "smart_ore_generation": {"version":[2, 0, 0], "name":"Stoupy's Smart Ore Generation", "url":"https://github.com/Stoupy51/SmartOreGeneration"},
	# "energy": {"version":[0, 6, 0], "name":"DatapackEnergy", "url":"https://github.com/ICY105/DatapackEnergy"},
	# "furnace_nbt_recipes": {"version":[2, 0, 0], "name":"Stoupy's Furnace NBT Recipes", "url":"https://github.com/Stoupy51/FurnaceNbtRecipes"},
}

# Other constants
ROOT = "/".join(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/").split("/")[:-1])
OVERRIDE_FOLDER = f"{ROOT}/override"
BUILD_FOLDER = f"{ROOT}/build"
TEXTURES_FOLDER = f"{ROOT}/textures"
DATABASE_FOLDER = f"{ROOT}/database"
DATAPACK_NAME = "ImagineYourCraft"
AUTHOR = "Stoupy51"
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"
BUILD_DATAPACK = f"{BUILD_FOLDER}/datapack"
BUILD_RESOURCE_PACK = f"{BUILD_FOLDER}/resource_pack"
MANUAL_PATH = f"{ROOT}/manual"
DATABASE = {}
EXTERNAL_DATABASE = {}		# Can be used to required an item from another datapack for a recipe or anything else
DATABASE_DEBUG = f"{ROOT}/database_debug.json"
MANUAL_DEBUG = f"{ROOT}/debug_manual.json"
SOURCE_LORE = f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]'
FACES = ("down", "up", "north", "south", "west", "east")
SIDES = ("_bottom", "_top", "_front", "_back", "_left", "_right", "_side")
OPENGL_RESOLUTION = 64
CPU_THREADS = int(os.cpu_count() * 0.75)	# 75% of the CPU threads

# Technical constants
CUSTOM_BLOCK_VANILLA = "minecraft:furnace"
CUSTOM_ENTITY_VANILLA = "minecraft:item_frame" # Useful for blocks that can be placed on walls or on player's position
CUSTOM_ITEM_VANILLA = "minecraft:command_block"
RESULT_OF_CRAFTING = "result_of_crafting"
USED_FOR_CRAFTING = "used_for_crafting"	# Should not be wrote manually unless you are crafting a vanilla item (ex: imagineyourcraft.chainmail -> chainmail armor)
CATEGORY = "category" # Key for the category, ex: "category":"material" or "category":"equipment"
MISC = "miscellaneous"
MODEL_DISPLAY = {"head":{"rotation":[0,0,0],"translation":[0,-30.42,0],"scale":[1.605,1.605,1.605]},"fixed":{"rotation":[-90,0,0],"translation":[0,0,-16],"scale":[2.0075,2.0075,2.0075]}}
NOT_COMPONENTS = ["id", "wiki", CATEGORY, RESULT_OF_CRAFTING, USED_FOR_CRAFTING]
VANILLA_ITEMS = ["emerald","stone"]
MAX_ITEMS_PER_ROW = 5	# Max number of items per row in the manual
MAX_ROWS_PER_PAGE = 6	# Max number of rows per page in the manual

# UUIDs for attribute modifiers to avoid conflicts
UUIDS = {
	"attack_damage":		{"helmet": [0,1,2,3], "chestplate": [0,4,5,6], "leggings": [0,7,8,9], "boots": [0,10,11,12], "sword": [0,13,14,15], "pickaxe": [0,16,17,18], "axe": [0,19,20,21], "shovel": [0,22,23,24], "hoe": [0,25,26,27]},
	"attack_speed":			{"helmet": [1,1,2,3], "chestplate": [1,4,5,6], "leggings": [1,7,8,9], "boots": [1,10,11,12], "sword": [1,13,14,15], "pickaxe": [1,16,17,18], "axe": [1,19,20,21], "shovel": [1,22,23,24], "hoe": [1,25,26,27]},
	"armor":				{"helmet": [2,1,2,3], "chestplate": [2,4,5,6], "leggings": [2,7,8,9], "boots": [2,10,11,12], "sword": [2,13,14,15], "pickaxe": [2,16,17,18], "axe": [2,19,20,21], "shovel": [2,22,23,24], "hoe": [2,25,26,27]},
	"armor_toughness":		{"helmet": [3,1,2,3], "chestplate": [3,4,5,6], "leggings": [3,7,8,9], "boots": [3,10,11,12], "sword": [3,13,14,15], "pickaxe": [3,16,17,18], "axe": [3,19,20,21], "shovel": [3,22,23,24], "hoe": [3,25,26,27]},
	"knockback_resistance":	{"helmet": [4,1,2,3], "chestplate": [4,4,5,6], "leggings": [4,7,8,9], "boots": [4,10,11,12], "sword": [4,13,14,15], "pickaxe": [4,16,17,18], "axe": [4,19,20,21], "shovel": [4,22,23,24], "hoe": [4,25,26,27]},
	"luck":					{"helmet": [5,1,2,3], "chestplate": [5,4,5,6], "leggings": [5,7,8,9], "boots": [5,10,11,12], "sword": [5,13,14,15], "pickaxe": [5,16,17,18], "axe": [5,19,20,21], "shovel": [5,22,23,24], "hoe": [5,25,26,27]},
	"mining_speed":			{"helmet": [6,1,2,3], "chestplate": [6,4,5,6], "leggings": [6,7,8,9], "boots": [6,10,11,12], "sword": [6,13,14,15], "pickaxe": [6,16,17,18], "axe": [6,19,20,21], "shovel": [6,22,23,24], "hoe": [6,25,26,27]},
	"gravity":				{"helmet": [7,1,2,3], "chestplate": [7,4,5,6], "leggings": [7,7,8,9], "boots": [7,10,11,12], "sword": [7,13,14,15], "pickaxe": [7,16,17,18], "axe": [7,19,20,21], "shovel": [7,22,23,24], "hoe": [7,25,26,27]},
}

# For easy testing (can be an empty list)
BUILD_COPY_DESTINATIONS = ("D:/latest_snapshot/world/datapacks", "D:/minecraft/snapshot/resourcepacks")

