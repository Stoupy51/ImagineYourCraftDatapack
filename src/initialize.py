
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *
import shutil

# Delete build folder and database_debug
print()
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
shutil.rmtree(DATABASE_DEBUG, ignore_errors=True)


# Setup pack.mcmeta for the datapack
with super_open(f"{BUILD_DATAPACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	super_json_dump(pack_mcmeta, file)
	info(f"pack.mcmeta file created for datapack")
	pass

# Setup pack.mcmeta for the resource pack
with super_open(f"{BUILD_RESOURCE_PACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": RESOURCE_PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	super_json_dump(pack_mcmeta, file)
	info(f"pack.mcmeta file created for resource pack")
	pass


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
for root, _, files in os.walk(TEXTURES_FOLDER):
	for file in files:
		if not file.endswith(".png"):
			continue
		new_name = file.lower()
		for k, v in REPLACEMENTS.items():
			if k in file:
				new_name = new_name.replace(k, v)
		if new_name != file:
			os.rename(f"{root}/{file}", f"{root}/{new_name}")
			info(f"Renamed {file} to {new_name}")
	pass

