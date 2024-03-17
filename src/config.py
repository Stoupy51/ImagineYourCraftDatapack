
# Imports
from io import TextIOWrapper
import os

# Datapack related constants
MINECRAFT_VERSION = "24w11a" # 1.20.5 snapshot
VERSION = "0.0.1"
NAMESPACE = "imagineyourcraft"
GLOBAL_NAMESPACE = "stoupy"
PACK_FORMAT = 33
RESOURCE_PACK_FORMAT = 28
DATA_VERSION = 3823	# 24w11a

# Other constants
BUILD_FOLDER = "build"
NAME = "ImagineYourCraft"
AUTHOR = "Stoupy51"
DESCRIPTION = f"{NAME} [{VERSION}] by {AUTHOR}"

# For easy file management
def super_open(file_path: str, mode: str) -> TextIOWrapper:
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

