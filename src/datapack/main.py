
# Import config
from src.importer import *
print()

# Generate datapack loading
import src.datapack.loading

# Generate items loot tables
import src.datapack.loot_tables

# TODO: Custom Blocks (place + destroy)
# TODO: Custom Ores generation

# Generate custom recipes
import src.datapack.recipes
info("Datapack successfully generated!")

