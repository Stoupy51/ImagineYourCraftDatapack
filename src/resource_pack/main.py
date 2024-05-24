
# Import config
from src.importer import *
print()

# Add the sounds folder to the resource pack
import src.resource_pack.sounds

# For each item, copy textures and make models
import src.resource_pack.item_models

# For each vanilla ID, create the json model file
import src.resource_pack.vanilla_models

