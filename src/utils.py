
from src.config import *
import json
import io

# Function mainly used for database generation
def ingr_repr(id: str, count: int|None = None) -> dict:
	""" Get the identity of the ingredient from its id for custom crafts
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts,
			ex: "custom_data": "imagineyourcraft.adamantium_ingot"
			ex: "item": "minecraft:stick"
	"""
	field = "item" if ":" in id else "custom_data"
	new_id = id if ":" in id else f"{NAMESPACE}.{id}"
	if count is None:
		return {field: new_id}
	else:
		return {"count": count, field: new_id}


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


# For nothing really special
def shuffled(lst: list) -> list:
	""" Return a shuffled version of the given list
	Args:
		lst	(list): The list to shuffle
	Returns:
		list: The shuffled list
	"""
	lst = lst.copy()
	random.shuffle(lst)
	return lst

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
	content = json.dumps(data, indent = '\t')
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

