
import shutil
import json
import os
import io

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
	if "/" in file_path or "\\" in file_path:
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


# Merge two dict recuirsively
def super_merge_dict(dict1: dict, dict2: dict) -> dict:
	""" Merge the two dictionnaries recursively without modifying originals
	Args:
		dict1 (dict): The first dictionnary
		dict2 (dict): The second dictionnary
	Returns:
		dict: The merged dictionnary
	"""
	# Copy first dictionnary
	new_dict = {}
	for key, value in dict1.items():
		new_dict[key] = value
	
	# For each key of the second dictionnary,
	for key, value in dict2.items():

		# If key exists in dict1, and both values are also dict, merge recursively
		if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
			new_dict[key] = super_merge_dict(dict1[key], value)
		
		# Else, just overwrite or add value
		else:
			new_dict[key] = value
	
	# Return the new dict
	return new_dict

# The majority of files will be written at the end of the program to prevent excessive disk access (reading + appending + writing)
FILES_TO_WRITE: dict[str, str] = {}
def write_to_file(file_path: str, content: str):
	if file_path not in FILES_TO_WRITE:
		FILES_TO_WRITE[file_path] = ""
	FILES_TO_WRITE[file_path] += str(content)
def write_all_files():
	for file_path, content in FILES_TO_WRITE.items():
		with super_open(file_path, "w") as f:
			f.write(content)

