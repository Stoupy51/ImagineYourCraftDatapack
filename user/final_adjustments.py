
# Imports
from config import *
from user.configurables import *
from src.utils.print import *

# For every key, apply common data and remove unused keys
i = 0
for k in DATABASE.keys():

	# Remove craft if not
	if DATABASE[k].get(RESULT_OF_CRAFTING) == []:
		del DATABASE[k][RESULT_OF_CRAFTING]
	
	# Make custom data if not made
	if not DATABASE[k].get("custom_data"):
		DATABASE[k]["custom_data"] = {}
	
	# Make display for every item
	item_str = k.replace("_"," ").title()
	if not DATABASE[k].get("item_name"):
		DATABASE[k]["item_name"] = f'[{{"text":"{item_str}","italic":false,"color":"white"}}]' 
	if SOURCE_LORE:
		if not DATABASE[k].get("lore"):
			DATABASE[k]["lore"] = []
		DATABASE[k]["lore"].append(SOURCE_LORE)
	if not DATABASE[k].get("custom_model_data"):
		DATABASE[k]["custom_model_data"] = STARTING_CMD + i
		if any(k in texture and "_on" in texture for texture in all_textures):
			i += 2
		else:
			i += 1

	# Private custom_data for namespace
	DATABASE[k]["custom_data"][NAMESPACE] = {k: True}

	# Smithed ignore vanilla behaviours
	if not DATABASE[k]["custom_data"].get("smithed"):
		DATABASE[k]["custom_data"]["smithed"] = {}
	DATABASE[k]["custom_data"]["smithed"]["ignore"] = {"functionality": True, "crafting": True}
info("Final adjustments applied")

