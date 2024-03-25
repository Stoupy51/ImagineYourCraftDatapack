
# Imports
from src.importer import *
"""{
	"music.game.conseil1": { "category": "music", "sounds": [ { "name": "survivor/conseil1", "stream": true } ] },
	"music.game.conseil2": { "category": "music", "sounds": [ { "name": "survivor/conseil2", "stream": true } ] },
	"music.game.conseil3": { "category": "music", "sounds": [ { "name": "survivor/conseil3", "stream": true } ] },
	"music.game.conseil4": { "category": "music", "sounds": [ { "name": "survivor/conseil4", "stream": true } ] }
}
"""
# Not Usable Records
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
				"custom_name": f'[{{"text":"{item_str}","italic":false,"color":"white"}}]'
			}

			# Add to sounds
			sounds[record] = {"category": "music", "sounds": [{"name": f"{NAMESPACE}/{record}","stream": True}]}
			super_copy(f"{root}/{file}", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds/{record}.ogg")

			# Next
			i += 1
	pass

# Write sounds.json
with super_open(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds.json", "w") as f:
	super_json_dump(sounds, f, max_level = 1)
	info("Sounds added to file :" + f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds.json")

info("Records added")

