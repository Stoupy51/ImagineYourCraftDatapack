
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *

# For each custom block
for item, data in DATABASE.items():
	if data["id"] == CUSTOM_BLOCK_VANILLA:

		path = f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/custom_blocks/{item}/place.mcfunction"

info("All customs blocks are now placeable and destroyable!")

