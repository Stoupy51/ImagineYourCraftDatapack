
# Imports
from src.importer import *
from database.configurables import *

# Print not used textures
textures_filenames = [texture for texture in textures_filenames if not DATABASE.get(texture.replace(".png",""))]
not_used = ""
for texture in textures_filenames:
	path = f"{TEXTURES_FOLDER}/{texture}".replace(f"{ROOT}/","")
	not_used += (f"\n'{path}' not found in the database")
	pass
if not_used:
	warning("Some textures not used in the database: " + not_used)

# Print a few keys of the database
info("Database generated, here are some keys: " + ", ".join(shuffled(list(DATABASE.keys()))[:7]) + "...")

# Export database to JSON for debugging generation
with open(DATABASE_DEBUG, "w") as f:
	super_json_dump(DATABASE, f)
	pass
