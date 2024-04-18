
# Import config
from src.importer import *

# Copy override folder content to build
print()
if os.path.exists(f"{OVERRIDE_FOLDER}"):
	shutil.copytree(f"{OVERRIDE_FOLDER}", f"{BUILD_FOLDER}", dirs_exist_ok = True)
	info(f"Override folder content copied to build folder")

# Add a small header for each .mcfunction file
import src.datapack.headers

# Generate zip files
datapack_path = f"{BUILD_FOLDER}/{DATAPACK_NAME}_datapack"
resourcepack_path = f"{BUILD_FOLDER}/{DATAPACK_NAME}_resource_pack"
if os.path.exists(BUILD_DATAPACK):
	shutil.make_archive(datapack_path, 'zip', BUILD_DATAPACK)
	debug(f"Datapack zip file generated at '{datapack_path.replace(f'{ROOT}/','')}.zip'")
else:
	warning(f"Datapack folder not found at '{BUILD_DATAPACK.replace(f'{ROOT}/','')}'")

if os.path.exists(BUILD_RESOURCE_PACK):
	shutil.make_archive(resourcepack_path, 'zip', BUILD_RESOURCE_PACK)
	debug(f"Resource pack zip file generated at '{resourcepack_path.replace(f'{ROOT}/','')}.zip'")
else:
	warning(f"Resource pack folder not found at '{BUILD_RESOURCE_PACK.replace(f'{ROOT}/','')}'")


# Copy datapack and resource pack to a specific location
try:
	super_copy(datapack_path + ".zip", BUILD_COPY_DESTINATIONS[0])
	debug(f"Datapack zip file copied to '{BUILD_COPY_DESTINATIONS[0]}/'")

	# Copy libraries
	for root, dirs, files in os.walk(f"{ROOT}/libs"):
		for file in files:
			if file.endswith(".zip"):
				super_copy(f"{root}/{file}", BUILD_COPY_DESTINATIONS[0])
				info(f"Library '{file}' copied to '{BUILD_COPY_DESTINATIONS[0]}/'")
except:
	warning(f"Could not copy datapack to '{BUILD_COPY_DESTINATIONS[0]}/'")
try:
	super_copy(resourcepack_path + ".zip", BUILD_COPY_DESTINATIONS[1])
	debug(f"Resource pack zip file copied to '{BUILD_COPY_DESTINATIONS[1]}/'")
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

