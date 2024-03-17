
# Imports
from src.config import *
import json

# Setup pack.mcmeta
with super_open(f"{BUILD_DATAPACK}/pack.mcmeta", "w") as file:
	pack_mcmeta =  {"pack":{"pack_format": PACK_FORMAT, "description": DESCRIPTION}, "id": NAMESPACE}
	json.dump(pack_mcmeta, file, indent = '\t')
	file.write("\n")



