
# Imports
from config import *
from database.configurables import *
from src.utils.print import *
from src.utils.io import *
import random
random.seed(3)

# Print not used textures
textures_filenames = [texture for texture in textures_filenames if not DATABASE.get(texture.replace(".png",""))]
not_used = ""
for texture in textures_filenames:
	path = f"{ASSETS_FOLDER}/{texture}".replace(f"{ROOT}/","")
	not_used += (f"\n'{path}' not found in the database")
	pass
if not_used:
	warning("Some textures are not used in the database: " + not_used)

# Print a few keys of the database
lst = list(DATABASE.keys())
random.shuffle(lst)
debug("Database generated, here are some keys:\n" + ", ".join(lst[:8]) + "...")

# Export database to JSON for debugging generation
with super_open(DATABASE_DEBUG, "w") as f:
	super_json_dump(DATABASE, f)

