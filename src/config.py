
# Imports
import datetime
import random
import os

# Import time constant and enable colors in Windows 10 console
IMPORT_TIME = datetime.datetime.now()
os.system("color")

# Datapack related constants
MINECRAFT_VERSION = "24w12a" # 1.20.5 snapshot
VERSION = "0.0.1"
NAMESPACE = "imagineyourcraft"
GLOBAL_NAMESPACE = "stoupy"
PACK_FORMAT = 34
RESOURCE_PACK_FORMAT = 29
DATA_VERSION = 3823	# 24w11a
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
DATABASE = {}
DATABASE_DEBUG = f"{DATABASE_FOLDER}/database_debug.json"
SOURCE_LORE = f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]'
FACES = ("down", "up", "north", "south", "west", "east")
SIDES = ("_bottom", "_top", "_front", "_back", "_left", "_right", "_side")


# Technical constants
CUSTOM_BLOCK_VANILLA = "minecraft:furnace"
CUSTOM_ITEM_VANILLA = "minecraft:command_block"
RESULT_OF_CRAFTING = "result_of_crafting"
USED_FOR_CRAFTING = "used_for_crafting"	# Should not be wrote manually unless you are crafting a vanilla item (ex: imagineyourcraft.chainmail -> chainmail armor)
MODEL_DISPLAY = {"head":{"rotation":[0,0,0],"translation":[0,-30.42,0],"scale":[1.605,1.605,1.605]},"fixed":{"rotation":[-90,0,0],"translation":[0,0,-16],"scale":[2.0075,2.0075,2.0075]}}
NOT_COMPONENTS = ["id", "wiki", RESULT_OF_CRAFTING, USED_FOR_CRAFTING]
VANILLA_ITEMS = ["emerald"]
random.seed(3)

# For easy testing (can be an empty list)
BUILD_COPY_DESTINATIONS = ("D:/latest_snapshot/world/datapacks", "C:/Users/Alexandre-PC/AppData/Roaming/.minecraft/1.13+/resourcepacks")

