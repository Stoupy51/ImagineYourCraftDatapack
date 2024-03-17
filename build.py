
# Imports
from src.config import *

# Delete build folder
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)

# Setup pack.mcmeta
with super_open(f"{BUILD_DATAPACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	json.dump(pack_mcmeta, file, indent = '\t')
	file.write("\n")
	pass


# Copy override folder content to build
if os.path.exists(f"{ROOT}/{OVERRIDE_FOLDER}"):
	shutil.copytree(f"{ROOT}/{OVERRIDE_FOLDER}", f"{ROOT}/{BUILD_FOLDER}", dirs_exist_ok = True)

# Finalyze build process
from src.finalyze import *

