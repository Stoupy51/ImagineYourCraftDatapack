
from src.config import *
import shutil
import json
import sys
import io

# Function mainly used for database generation
def ingr_repr(id: str, count: int|None = None) -> dict:
	""" Get the identity of the ingredient from its id for custom crafts
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts,
			ex: {"components":{"custom_data":{imagineyourcraft:{adamantium_ingot=True}}}}
			ex: {"item": "minecraft:stick"}
	"""
	if ":" in id:
		to_return = {"item": id}
	else:
		to_return = {"components":{"custom_data":{NAMESPACE:{id:True}}}}
	if count is not None:
		to_return["count"] = count
	return to_return

def ingr_to_id(ingredient: dict, add_namespace: bool = True) -> str:
	""" Get the id from an ingredient dict
	Args:
		ingredient (dict): The ingredient dict
			ex: {"components":{"custom_data":{imagineyourcraft:{adamantium_ingot=True}}}}
			ex: {"item": "minecraft:stick"}
	Returns:
		str: The id of the ingredient, ex: "minecraft:stick" or "imagineyourcraft:adamantium_ingot"
	"""
	if ingredient.get("item"):
		if not add_namespace:
			return ingredient["item"].split(":")[1]
		return ingredient["item"]
	else:
		custom_data = ingredient["components"]["custom_data"]
		namespace = list(custom_data.keys())[0]
		id = list(custom_data[namespace].keys())[0]
		if add_namespace:
			return namespace + ":" + id
		return id


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
	if "b" in mode:
		return open(file_path, mode)
	else:
		return open(file_path, mode, encoding = "utf-8") # Always use utf-8 encoding to avoid issues


# For easy file copy
def super_copy(src: str, dst: str) -> shutil.copy:
	""" Copy a file from the source to the destination
	Args:
		src	(str): The source file path
		dst	(str): The destination file path
	"""
	# Make directory
	os.makedirs(os.path.dirname(dst), exist_ok=True)

	# Copy file
	return shutil.copy(src, dst)


# JSON dump with indentation for levels
def super_json_dump(data: dict|list, file: io.TextIOWrapper = None, max_level: int = 2) -> str:
	""" Dump the given data to a JSON file with indentation for only 2 levels by default
	Args:
		data (dict|list): 			The data to dump
		file (io.TextIOWrapper): 	The file to dump the data to, if None, the data is returned as a string
		max_level (int):			The level of where indentation should stop (-1 for infinite)
	Returns:
		str: The content of the file in every case
	"""
	content = json.dumps(data, indent = '\t', ensure_ascii = False)
	if max_level > -1:

		# Seek in content to remove to high indentations
		longest_indentation = 0
		for line in content.split("\n"):
			indentation = 0
			for char in line:
				if char == "\t":
					indentation += 1
				else:
					break
			longest_indentation = max(longest_indentation, indentation)
		for i in range(longest_indentation, max_level, -1):
			content = content.replace("\n" + "\t" * i, "")
			pass

		# To finalyze, fix the last indentations
		finishes = ('}', ']')
		for char in finishes:
			to_replace = "\n" + "\t" * max_level + char
			content = content.replace(to_replace, char)
	
	# Write file content and return it
	content += "\n"
	if file:
		file.write(content)
	return content


# Exporting database
def export_database(path: str = DATABASE_DEBUG) -> None:
	""" Export the database to a JSON file for debugging generation
	Args:
		path (str): The path to the JSON file (optional)
	"""
	with super_open(path, "w") as f:
		super_json_dump(DATABASE, f)
	return


# Colors constants
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
def current_time() -> str:
	return datetime.datetime.now().strftime("%H:%M:%S")
def info(text: str = "") -> None:
	print(f"{GREEN}[INFO  {current_time()}] {text}{RESET}")
def debug(text: str = "") -> None:
	print(f"{BLUE}[DEBUG {current_time()}] {text}{RESET}")
def warning(text: str = "") -> None:
	print(f"{YELLOW}[WARNING {current_time()}] {text}{RESET}")
def error(text: str = "", exit: bool = True) -> None:
	print(f"{RED}[ERROR {current_time()}] {text}{RESET}")
	if exit:
		sys.exit(1)

