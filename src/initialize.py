
# Import config
from src.config import *

# Delete build folder and database_debug
print()
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
shutil.rmtree(DATABASE_DEBUG, ignore_errors=True)


# Setup pack.mcmeta
with super_open(f"{BUILD_DATAPACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	json.dump(pack_mcmeta, file, indent = '\t')
	file.write("\n")
	info(f"pack.mcmeta file created")
	pass


