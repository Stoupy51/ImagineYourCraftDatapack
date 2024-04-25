
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *
import shutil

# Copy override folder content to build
print()
if os.path.exists(f"{OVERRIDE_FOLDER}"):
	shutil.copytree(f"{OVERRIDE_FOLDER}", f"{BUILD_FOLDER}", dirs_exist_ok = True)
	info(f"Override folder content copied to build folder")


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
		super_copy(f"{destination}.zip", f"{copy_destination}/{file}")
		debug(f"'{dest_no_root}.zip' file copied to '{copy_destination}/{file}'")
	except:
		warning(f"Unable to copy '{dest_no_root}.zip' to '{copy_destination}'")


# Copy datapack libraries
try:
	for root, dirs, files in os.walk(f"{ROOT}/libs"):
		for file in files:
			if file.endswith(".zip"):
				super_copy(f"{root}/{file}", BUILD_COPY_DESTINATIONS[0])
				info(f"Library '{file}' copied to '{BUILD_COPY_DESTINATIONS[0]}/'")
except:
	warning(f"Could not copy datapack libraries to '{BUILD_COPY_DESTINATIONS[0]}/'")

# Remove __pycache__ folders because they are annoying
for root, dirs, files in os.walk(ROOT):
	for dir in dirs:
		if dir == "__pycache__":
			shutil.rmtree(os.path.join(root, dir))
	pass

