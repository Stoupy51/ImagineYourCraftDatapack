
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *
import shutil

# For every file in the merge folder, copy it to the build folder (with append content)
print()
for root, _, files in os.walk(MERGE_FOLDER):
	for file in files:
		merge_path = f"{root}/{file}".replace("\\", "/")
		build_path = merge_path.replace(MERGE_FOLDER, BUILD_FOLDER)
		
		# Append content to the build file is any
		if os.path.isfile(build_path):

			# If file is not JSON format,
			if not file.endswith(".json"):
				with super_open(merge_path, "r") as f:
					content = f.read()
				with super_open(build_path, "a") as f:
					f.write(content)

			else:
				# Load to two dictionnaries
				with super_open(merge_path, "r") as f:
					merge_dict = json.load(f)
				with super_open(build_path, "r") as f:
					build_dict = json.load(f)
				
				# Write the merged dictionnaries to the build file
				with super_open(build_path, "w") as f:
					super_json_dump(super_merge_dict(build_dict, merge_dict), -1)
		else:
			super_copy(merge_path, build_path)
info(f"All content in the '{MERGE_FOLDER.replace(ROOT, '')}' folder copied to '{BUILD_FOLDER.replace(ROOT, '')}'")


# Add a small header for each .mcfunction file
import src.datapack.headers


# Generate zip files
processes = [
	(BUILD_DATAPACK, f"{BUILD_FOLDER}/{DATAPACK_NAME}_datapack", BUILD_COPY_DESTINATIONS[0]),
	(BUILD_RESOURCE_PACK, f"{BUILD_FOLDER}/{DATAPACK_NAME}_resource_pack", BUILD_COPY_DESTINATIONS[1])
]
for source, destination, copy_destination in processes:
	source_no_root = source.replace(f"{ROOT}/", "")
	dest_no_root = destination.replace(f"{ROOT}/", "")
	if os.path.exists(source):
		shutil.make_archive(destination, 'zip', source)
		debug(f"'{dest_no_root}.zip' file generated")
	else:
		warning(f"'{source_no_root}' folder not found")
	try:
		file = f"{dest_no_root}.zip".split("/")[-1]
		shutil.copy(f"{destination}.zip", f"{copy_destination}/{file}")
		debug(f"'{dest_no_root}.zip' file copied to '{copy_destination}/{file}'")
	except:
		warning(f"Unable to copy '{dest_no_root}.zip' to '{copy_destination}'")


# Copy datapack libraries
try:
	for root, dirs, files in os.walk(f"{ROOT}/libs"):
		for file in files:
			if file.endswith(".zip"):
				shutil.copy(f"{root}/{file}", BUILD_COPY_DESTINATIONS[0])
				info(f"Library '{file}' copied to '{BUILD_COPY_DESTINATIONS[0]}/'")
except:
	warning(f"Could not copy datapack libraries to '{BUILD_COPY_DESTINATIONS[0]}/'")

# Remove __pycache__ folders because they are annoying
for root, dirs, files in os.walk(ROOT):
	for dir in dirs:
		if dir == "__pycache__":
			shutil.rmtree(os.path.join(root, dir))
	pass

