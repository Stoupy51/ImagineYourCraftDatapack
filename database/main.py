
# This python script tries generates a database of every block and item by using checking the textures folder
# It should be imported to fill the DATABASE variable
from src.importer import *
from database.configurables import *
from database.additions import *

# Generate ores in database
from database.insert_ores import *

# Apply database additions
for k, v in database_additions.items():
	if k in DATABASE:
		DATABASE[k].update(v)
	else:
		DATABASE[k] = v

# For every key
for k in DATABASE.keys():

	# Remove craft if not
	if DATABASE[k].get(CRAFTING_RECIPES) == []:
		del DATABASE[k][CRAFTING_RECIPES]
	
	# Make custom data if not made
	if not DATABASE[k].get("custom_data"):
		DATABASE[k]["custom_data"] = {}
	
	# Make display for every item
	item_str = k.replace("_"," ").title()
	DATABASE[k]["custom_name"] = f'[{{"text":"{item_str}","italic":false,"color":"white"}}]' 
	if not DATABASE[k].get("lore"):
		DATABASE[k]["lore"] = []
	DATABASE[k]["lore"].append(SOURCE_LORE)
	if not DATABASE[k].get("custom_model_data"):
		DATABASE[k]["custom_model_data"] = "PREFIX_XXX"

	# Private custom_data for namespace
	DATABASE[k]["custom_data"][NAMESPACE] = {k: 1}

	# Smithed ignore vanilla behaviours
	if not DATABASE[k]["custom_data"].get("smithed"):
		DATABASE[k]["custom_data"]["smithed"] = {}
	DATABASE[k]["custom_data"]["smithed"]["ignore"] = {"functionality": 1, "crafting": 1}

# Print not used textures and then all the keys
textures_filenames = [texture for texture in textures_filenames if not DATABASE.get(texture.replace(".png",""))]

for texture in textures_filenames:
	path = f"{TEXTURES_FOLDER}/{texture}".replace(f"{ROOT}/","")
	warning(f"Texture '{path}' is not used in the database")
	pass
info("Database generated, here are the keys: " + ", ".join(shuffled(list(DATABASE.keys()))[:7]) + "...")

# Export database to JSON for debugging generation
with open(DATABASE_DEBUG, "w") as f:
	super_json_dump(DATABASE, f)
	pass

