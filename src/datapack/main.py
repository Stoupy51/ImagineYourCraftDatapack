
# Import config
from src.config import *
from src.utils.print import *
print()

# Generate datapack loading
import src.datapack.loading

# Generate items loot tables
import src.datapack.loot_tables

# TODO: Custom Blocks (place + destroy)
import src.datapack.custom_blocks
# TODO: Custom Ores generation

# Generate custom recipes
import src.datapack.recipes
info("Datapack successfully generated!")

