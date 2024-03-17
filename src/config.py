
# Imports
import datetime
import imageio
import random
import shutil
import json
import io
import os

# Import time constant
IMPORT_TIME = datetime.datetime.now()

# Colors constants
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
def current_time() -> str:
	return datetime.datetime.now().strftime("%H:%M:%S")
def info(text: str) -> None:
	print(f"{GREEN}[INFO {current_time()}] {text}{RESET}")
def warning(text: str) -> None:
	print(f"{YELLOW}[WARNING {current_time()}] {text}{RESET}")
def error(text: str) -> None:
	print(f"{RED}[ERROR {current_time()}] {text}{RESET}")

# Datapack related constants
MINECRAFT_VERSION = "24w11a" # 1.20.5 snapshot
VERSION = "0.0.1"
NAMESPACE = "imagineyourcraft"
GLOBAL_NAMESPACE = "stoupy"
PACK_FORMAT = 33
RESOURCE_PACK_FORMAT = 28
DATA_VERSION = 3823	# 24w11a

# Other constants
ROOT = "/".join(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/").split("/")[:-1])
OVERRIDE_FOLDER = f"{ROOT}/override"
BUILD_FOLDER = f"{ROOT}/build"
TEXTURES_FOLDER = f"{ROOT}/textures"
DATAPACK_NAME = "ImagineYourCraft"
AUTHOR = "Stoupy51"
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"
BUILD_DATAPACK = f"{BUILD_FOLDER}/datapack"
BUILD_RESOURCE_PACK = f"{BUILD_FOLDER}/resource_pack"
BUILD_COPY_DESTINATIONS = ("D:/5) Energy System/world/datapacks", "C:/Users/Alexandre-PC/AppData/Roaming/.minecraft/1.13+/resourcepacks")
DATABASE = {}
DATABASE_DEBUG = "database_debug.json"
SOURCE_LORE = f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]'

# Technical constants
CUSTOM_BLOCK_VANILLA = "minecraft:barrel"
CUSTOM_ITEM_VANILLA = "minecraft:command_block"
CRAFTING_RECIPES = "result_of_crafting"

