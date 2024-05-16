
# Imports
from config import *
from src.utils.print import *
from src.utils.io import *

# Not Usable Records
# TODO, add official support
i = 1
sounds = {}
for root, dirs, files in os.walk(f"{ROOT}/textures/records"):
	for file in files:
		if file.endswith(".ogg") and dirs:

			# Create item in database
			record = f"record_{i}"
			item_str = file.replace(".ogg","")
			DATABASE[record] = {
				"id": CUSTOM_ITEM_VANILLA,
				"custom_data": {NAMESPACE:{record: True}},
				"item_name": f'[{{"text":"{item_str}","italic":false,"color":"white"}}]'
			}

			# Add to sounds
			sounds[record] = {"category": "music", "sounds": [{"name": f"{NAMESPACE}:{record}","stream": True}]}
			super_copy(f"{root}/{file}", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds/{record}.ogg")

			# Next
			i += 1
	pass

# Write sounds.json
write_to_file(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds.json", super_json_dump(sounds, max_level = 1))
info("Records added")
