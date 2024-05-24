
# Import config
from src.importer import *
from src.utils.io import *
from src.utils.print import *
import shutil

# Delete build folder and database_debug
print()
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
shutil.rmtree(DATABASE_DEBUG, ignore_errors=True)


# Setup pack.mcmeta for the datapack
pack_mcmeta =  {"pack":{"pack_format": DATAPACK_PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
write_to_file(f"{BUILD_DATAPACK}/pack.mcmeta", super_json_dump(pack_mcmeta))
info(f"pack.mcmeta file created for datapack")

# Setup pack.mcmeta for the resource pack
pack_mcmeta =  {"pack":{"pack_format": RESOURCE_PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
write_to_file(f"{BUILD_RESOURCE_PACK}/pack.mcmeta", super_json_dump(pack_mcmeta))
info(f"pack.mcmeta file created for resource pack")


# Convert textures names if needed
REPLACEMENTS = {
	"_off": "",
	"_down": "_bottom",
	"_up": "_top",
	"_north": "_front",
	"_south": "_back",
	"_west": "_left",
	"_east": "_right",
}
for file in TEXTURES_FILES:
	new_name = file.lower()
	for k, v in REPLACEMENTS.items():
		if k in file:
			new_name = new_name.replace(k, v)
	if new_name != file:
		os.rename(f"{TEXTURES_FOLDER}/{file}", f"{TEXTURES_FOLDER}/{new_name}")
		info(f"Renamed {file} to {new_name}")

