
# Import config
from src.config import *

# Copy override folder content to build
print()
if os.path.exists(f"{ROOT}/{OVERRIDE_FOLDER}"):
	shutil.copytree(f"{ROOT}/{OVERRIDE_FOLDER}", f"{ROOT}/{BUILD_FOLDER}", dirs_exist_ok = True)
	info(f"Override folder content copied to build folder")


# Generate zip files
datapack_path = f"{ROOT}/{BUILD_FOLDER}/{NAME}_datapack"
resourcepack_path = f"{ROOT}/{BUILD_FOLDER}/{NAME}_resource_pack"
if os.path.exists(BUILD_DATAPACK):
	shutil.make_archive(datapack_path, 'zip', BUILD_DATAPACK)
	info(f"Datapack zip file generated at '{datapack_path}.zip'")
else:
	warning(f"Datapack folder not found at '{BUILD_DATAPACK}'")

if os.path.exists(BUILD_RESOURCE_PACK):
	shutil.make_archive(resourcepack_path, 'zip', BUILD_RESOURCE_PACK)
	info(f"Resource pack zip file generated at '{resourcepack_path}.zip'")
else:
	warning(f"Resource pack folder not found at '{BUILD_RESOURCE_PACK}'")


# Copy datapack and resource pack to a specific location
if BUILD_COPY_DESTINATIONS and type(BUILD_COPY_DESTINATIONS) == tuple:
	if os.path.exists(datapack_path + ".zip"):
		if type(BUILD_COPY_DESTINATIONS[0]) == str:
			shutil.copy(datapack_path + ".zip", BUILD_COPY_DESTINATIONS[0])
			info(f"Datapack zip file copied to '{BUILD_COPY_DESTINATIONS[0]}'")
		else:
			warning("First copy destination is not a string")
	else:
		warning(f"Datapack zip file not found at '{datapack_path}.zip'")

	if os.path.exists(resourcepack_path + ".zip"):
		if type(BUILD_COPY_DESTINATIONS[1]) == str:
			shutil.copy(resourcepack_path + ".zip", BUILD_COPY_DESTINATIONS[1])
			info(f"Resource pack zip file copied to '{BUILD_COPY_DESTINATIONS[1]}'")
		else:
			warning("Second copy destination is not a string")
	else:
		warning(f"Resource pack zip file not found at '{resourcepack_path}.zip'")


# Remove __pycache__ folders because they are annoying
for root, dirs, files in os.walk(ROOT):
	for dir in dirs:
		if dir == "__pycache__":
			shutil.rmtree(os.path.join(root, dir))
	pass


# Finalyze build process
total_time = datetime.datetime.now() - IMPORT_TIME
info(f"Build finished in {total_time.total_seconds()} seconds\n")

