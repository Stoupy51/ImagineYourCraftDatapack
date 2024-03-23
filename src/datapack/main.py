
# Import config
from src.importer import *
print()

# Generate datapack loading
import src.datapack.loading

# Generate items loot tables
import src.datapack.loot_tables

# TODO: Basic structure (tick, second, minute)
# TODO: Custom Blocks (place + destroy)
# TODO: Custom Ores generation

# Generate custom recipes
import src.datapack.recipes_vanilla_input

# Finally, add a small header for each .mcfunction file
import src.datapack.headers
info("Datapack successfully generated!")

