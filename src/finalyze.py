
# Import config
from src.importer import *

# Copy override folder content to build
print()
if os.path.exists(f"{OVERRIDE_FOLDER}"):
	shutil.copytree(f"{OVERRIDE_FOLDER}", f"{BUILD_FOLDER}", dirs_exist_ok = True)
	info(f"Override folder content copied to build folder")


# Generate zip files
datapack_path = f"{BUILD_FOLDER}/{DATAPACK_NAME}_datapack"
resourcepack_path = f"{BUILD_FOLDER}/{DATAPACK_NAME}_resource_pack"
if os.path.exists(BUILD_DATAPACK):
	shutil.make_archive(datapack_path, 'zip', BUILD_DATAPACK)
	info(f"Datapack zip file generated at '{datapack_path.replace(f'{ROOT}/','')}.zip'")
else:
	warning(f"Datapack folder not found at '{BUILD_DATAPACK.replace(f'{ROOT}/','')}'")

if os.path.exists(BUILD_RESOURCE_PACK):
	shutil.make_archive(resourcepack_path, 'zip', BUILD_RESOURCE_PACK)
	info(f"Resource pack zip file generated at '{resourcepack_path.replace(f'{ROOT}/','')}.zip'")
else:
	warning(f"Resource pack folder not found at '{BUILD_RESOURCE_PACK.replace(f'{ROOT}/','')}'")


# Copy datapack and resource pack to a specific location
try:
	shutil.copy(datapack_path + ".zip", BUILD_COPY_DESTINATIONS[0])
	info(f"Datapack zip file copied to '{BUILD_COPY_DESTINATIONS[0]}/'")
except:
	warning(f"Could not copy datapack to '{BUILD_COPY_DESTINATIONS[0]}/'")
try:
	shutil.copy(resourcepack_path + ".zip", BUILD_COPY_DESTINATIONS[1])
	info(f"Resource pack zip file copied to '{BUILD_COPY_DESTINATIONS[1]}/'")
except:
	warning(f"Could not copy resource pack to '{BUILD_COPY_DESTINATIONS[1]}/'")

# Remove __pycache__ folders because they are annoying
for root, dirs, files in os.walk(ROOT):
	for dir in dirs:
		if dir == "__pycache__":
			shutil.rmtree(os.path.join(root, dir))
	pass


# Finalyze build process
total_time = datetime.datetime.now() - IMPORT_TIME
info(f"Build finished in {total_time.total_seconds()} seconds\n")

