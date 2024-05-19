
# Import config
from config import *
from src.utils.io import *
from src.utils.print import *

# Add the sounds folder to the resource pack
sounds_names = os.listdir(f"{ASSETS_FOLDER}/sounds")
if sounds_names:
	for sound in sounds_names:

		# Get sound without spaces and special characters
		sound_file = "".join(char for char in sound.replace(" ", "_") if char.isalnum() or char in "._").lower()
		super_copy(f"{ASSETS_FOLDER}/sounds/{sound}", f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds/{sound_file}")

		# Get sound without file extension
		sound = ".".join(sound.split(".")[:-1])
		sound_file = ".".join(sound_file.split(".")[:-1])

		# Add sound json to sounds.json
		sound_json = {sound_file: {"subtitle": sound, "sounds": [f"{NAMESPACE}:{sound_file}"]}}
		write_to_file(f"{BUILD_RESOURCE_PACK}/assets/{NAMESPACE}/sounds.json", super_json_dump(sound_json))	

	info(f"All sounds in '{ASSETS_FOLDER}/sounds/' have been copied to the resource pack")
