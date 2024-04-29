
# Import config
from src.config import *
from src.utils.print import *
print()

# Generate datapack loading
import src.datapack.loading

# Generate basic datapack structure (tick, tick_2, second, second_5, minute)
import src.datapack.basic_structure

# Custom Blocks (place + destroy)
import src.datapack.custom_blocks
# TODO: Custom Ores generation

# Generate items loot tables
import src.datapack.loot_tables

# Generate custom recipes
import src.datapack.recipes
info("Datapack successfully generated!")

