
# Import config
from src.importer import *

# Delete build folder and database_debug
print()
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
shutil.rmtree(DATABASE_DEBUG, ignore_errors=True)


# Setup pack.mcmeta for the datapack
with super_open(f"{BUILD_DATAPACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	json.dump(pack_mcmeta, file, indent = '\t')
	file.write("\n")
	info(f"pack.mcmeta file created")
	pass

# Setup pack.mcmeta for the resource pack
with super_open(f"{BUILD_RESOURCE_PACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": RESOURCE_PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	json.dump(pack_mcmeta, file, indent = '\t')
	file.write("\n")
	info(f"pack.mcmeta file created")
	pass


