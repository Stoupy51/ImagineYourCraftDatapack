
# Imports
import datetime
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
OVERRIDE_FOLDER = "override"
BUILD_FOLDER = "build"
NAME = "ImagineYourCraft"
AUTHOR = "Stoupy51"
DESCRIPTION = f"{NAME} [{VERSION}] by {AUTHOR}"
BUILD_COPY_DESTINATIONS = ("D:/5) Energy System/world/datapacks", "C:/Users/Alexandre-PC/AppData/Roaming/.minecraft/1.13+/resourcepacks")

# For easy file management
def super_open(file_path: str, mode: str) -> io.TextIOWrapper:
	""" Open a file with the given mode, creating the directory if it doesn't exist
	Args:
		file_path	(str): The path to the file
		mode		(str): The mode to open the file with, ex: "w", "r", "a", "wb", "rb", "ab"
	Returns:
		open: The file object, ready to be used
	"""
	# Make directory
	os.makedirs(os.path.dirname(file_path), exist_ok=True)

	# Open file and return
	return open(file_path, mode, encoding="utf-8") # Always use utf-8 encoding to avoid issues
ROOT = "/".join(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/").split("/")[:-1])
BUILD_DATAPACK = f"{ROOT}/{BUILD_FOLDER}/datapack"
BUILD_RESOURCE_PACK = f"{ROOT}/{BUILD_FOLDER}/resource_pack"

