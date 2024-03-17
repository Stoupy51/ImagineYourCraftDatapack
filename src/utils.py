
from src.config import *

# Function mainly used for database generation
def ingr_repr(id: str, count: int|None = None) -> dict:
	""" Get the identity of the ingredient from its id for custom crafts
	Args:
		id	(str): The id of the ingredient, ex: adamantium_ingot
	Returns:
		str: The identity of the ingredient for custom crafts, ex: "custom_data": "imagineyourcraft.adamantium_ingot"
	"""
	if count is None:
		return {"custom_data": f"{NAMESPACE}.{id}"}
	else:
		return {"Count": count, "custom_data": f"{NAMESPACE}.{id}"}


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

