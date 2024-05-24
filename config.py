
# Imports
import os

# Folders
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
MERGE_FOLDER: str = f"{ROOT}/merge"					# If a file exists in both merge and build folder, they will be merged. Otherwise, it's just copied.
MANUAL_PATH: str = f"{ROOT}/manual"					# Cached manual assets
BUILD_FOLDER: str = f"{ROOT}/build"					# Folder where the final datapack and resource pack are built
ASSETS_FOLDER: str = f"{ROOT}/assets"				# Folder containing the all assets (textures, sounds, ...) for the datapack
TEXTURES_FOLDER: str = f"{ASSETS_FOLDER}/textures"	# Folder containing the textures for the datapack
LIBS_FOLDER: str = f"{ROOT}/libs"					# The libraries are copied to the build destination, and merged with the datapack using Weld
BUILD_COPY_DESTINATIONS: tuple[str, str] = ("D:/latest_snapshot/world/datapacks", "D:/minecraft/snapshot/resourcepacks")	# Can be an empty list if you don't want to copy the generated files

# Assets files
ASSETS_FILES: list[str] = [f"{root}/{f}".replace("\\","/") for root, _, files in os.walk(ASSETS_FOLDER) for f in files]
TEXTURES_FILES: list[str] = [path.split(f"{TEXTURES_FOLDER}/")[1] for path in ASSETS_FILES if path.startswith(TEXTURES_FOLDER) and path.endswith(".png")]

# Dev constants
HAS_MANUAL: bool = True								# Do the program generate a manual/guide? (WARNING: if an item is malformed in the database, the server log will be flooded on load by the manual hiding the malformed item)
DEBUG_MODE: bool = False							# Shows up grids in manual,
DATABASE_DEBUG: str = f"{ROOT}/database_debug.json"	# Dump of the database for debugging purposes
CMD_CACHE: str = f"{ROOT}/cmd_cache.json"			# Cache of all items Custom Model Data
CACHE_MANUAL_ASSETS: bool = True					# Caches the MC assets and the items renders for the manual (manual/items/*.png)
CACHE_MANUAL_PAGES: bool = True						# Caches the content of the manual and the images (manual/pages/*.png)
MANUAL_DEBUG: str = f"{ROOT}/debug_manual.json"		# Dump of the manual for debugging purposes
ENABLE_TRANSLATIONS: bool = False					# Will convert all the text components to translate and generate a lang file (WARNING: The algorithm is pretty slow, so it's recommended to disable it when not needed)
LANG_FILE_DEBUG: str = f"{ROOT}/debug_lang.json"	# Dump of the lang file for debugging purposes
MERGE_LIBS: bool = False							# Make new zip of merged libraries with the datapack and resource pack using Smithed Weld


# Datapack related constants
AUTHOR: str = "Stoupy51"				# Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
DATAPACK_NAME: str = "ImagineYourCraft"	# Name of the datapack, used for messages and items lore
MINECRAFT_VERSION: str = "1.20.6"		# Text used when loading the datapack to warn the user when the data version is not right
DATA_VERSION: int = 3835				# Depending on MC version, given by /data get entity @p DataVersion to check if the datapack is not running in an older version of MC
VERSION: str = "0.0.1"					# Datapack version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "iyc"					# Should be the same you use in the merge folder. Used to namespace functions, tags, etc.
DATAPACK_PACK_FORMAT: int = 45			# Pack format version, see https://minecraft.wiki/w/Pack_format#List_of_data_pack_formats
RESOURCE_PACK_FORMAT: int = 34			# Resource pack format version, see https://minecraft.wiki/w/Pack_format#List_of_resource_pack_formats
MANUAL_NAME: str = f"{DATAPACK_NAME} Manual"				# Name of the manual, used for the title of the book and first page
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"	# Pack description displayed in pack.mcmeta
DEPENDENCIES: dict[str, dict[str, list[int] | str]] = {
	# Automagically, the datapack will check for the presence of dependencies and their minimum required versions at runtime
	# The url is used when the dependency is not found to suggest where to get it
	# The version dict key contains the minimum required version of the dependency in [major, minor, patch] format
	# The main key is the dependency namespace to check for
	# The name can be whatever you want, it's just used in messages

	"common_signals": {"version":[0, 0, 0], "name":"Common Signals", "url":"https://github.com/Stoupy51/CommonSignals"},
	"smithed.custom_block": {"version":[0, 3, 0], "name":"Smithed Custom Block Placement", "url":"https://wiki.smithed.dev/libraries/custom-block/"},
	#"smithed.crafter": {"version":[0, 3, 1], "name":"Smithed Crafter", "url":"https://wiki.smithed.dev/libraries/crafter/"},
	# "smart_ore_generation": {"version":[2, 0, 0], "name":"Stoupy's Smart Ore Generation", "url":"https://github.com/Stoupy51/SmartOreGeneration"},
	# "energy": {"version":[0, 6, 0], "name":"DatapackEnergy", "url":"https://github.com/ICY105/DatapackEnergy"},
	# "furnace_nbt_recipes": {"version":[2, 0, 0], "name":"Stoupy's Furnace NBT Recipes", "url":"https://github.com/Stoupy51/FurnaceNbtRecipes"},
}

# Technical constants
SOURCE_LORE: list[dict] = [{"text": DATAPACK_NAME,"italic":True,"color":"blue"}]	# Appended lore to any custom item, can be an empty string
MAX_ITEMS_PER_ROW: int = 5		# Max number of items per row in the manual, should not exceed 6
MAX_ROWS_PER_PAGE: int = 5		# Max number of rows per page in the manual, should not exceed 6
OPENGL_RESOLUTION: int = 64		# Resolution of the OpenGL renders used in the manual, best value is 64 <--- 64x64

# Text for the first page of the manual
if HAS_MANUAL:
	MANUAL_FIRST_PAGE_TEXT: dict = {"text":"This manual is very interactive and will guide you through the different items and blocks available in the datapack!", "color":"#505050"}

