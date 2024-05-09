
# Imports
import os

# Folders
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
MERGE_FOLDER: str = f"{ROOT}/merge"					# If a file exists in both merge and build folder, they will be merged. Otherwise, it's just copied.
MANUAL_PATH: str = f"{ROOT}/manual"					# Cached manual assets
BUILD_FOLDER: str = f"{ROOT}/build"					# Folder where the final datapack and resource pack are built
ASSETS_FOLDER: str = f"{ROOT}/assets"				# Folder containing the all assets (textures, sounds, ...) for the datapack
LIBS_FOLDER: str = f"{ROOT}/libs"					# The libraries are copied to the build destination, and merged with the datapack using Weld
BUILD_COPY_DESTINATIONS: tuple[str, str] = ("D:/latest_snapshot/world/datapacks", "D:/minecraft/snapshot/resourcepacks")	# Can be an empty list if you don't want to copy the generated files


# Dev constants
HAS_MANUAL: bool = True								# Do the program generate a manual/guide?
DEBUG_MODE: bool = True								# Shows up grids in manual,
DATABASE_DEBUG: str = f"{ROOT}/database_debug.json"	# Dump of the database for debugging purposes
CACHE_MANUAL_ASSETS: bool = True					# Caches the MC assets and the items renders for the manual (manual/items/*.png)
CACHE_MANUAL_PAGES: bool = True						# Caches the content of the manual and the images (manual/pages/*.png)
MANUAL_DEBUG: str = f"{ROOT}/debug_manual.json"		# Dump of the manual for debugging purposes
MERGE_LIBS: bool = False							# Make new zip of merged libraries with the datapack and resource pack using Smithed Weld


# Datapack related constants
AUTHOR: str = "Stoupy51"				# Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
DATAPACK_NAME: str = "ImagineYourCraft"	# Name of the datapack, used for messages and items lore
DATAPACK_NAME_SIMPLE: str = "".join([c for c in DATAPACK_NAME if c.isalnum()])	# Simplified version of the datapack name, used for paths
MINECRAFT_VERSION: str = "1.20.6"		# Text used when loading the datapack to warn the user when the data version is not right
DATA_VERSION: int = 3835				# Depending on MC version, given by /data get entity @p DataVersion to check if the datapack is not running in an older version of MC
VERSION: str = "0.0.1"					# Datapack version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "iyc"					# Should be the same you use in the merge folder. Used to namespace functions, tags, etc.
PACK_FORMAT: int = 41					# Pack format version, see https://minecraft.wiki/w/Pack_format#List_of_data_pack_formats
RESOURCE_PACK_FORMAT: int = 32			# Resource pack format version, see https://minecraft.wiki/w/Pack_format#List_of_resource_pack_formats
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"	# Pack description displayed in pack.mcmeta
DEPENDENCIES: dict[str, dict[str, list[int] | str]] = {
	# Automagically, the datapack will check for the presence of dependencies and their minimum required versions at runtime
	# The url is used when the dependency is not found to suggest where to get it
	# The version dict key contains the minimum required version of the dependency in [major, minor, patch] format
	# The main key is the dependency namespace to check for
	# The name can be whatever you want, it's just used in messages

	"common_signals": {"version":[0, 0, 0], "name":"Common Signals", "url":"https://github.com/Stoupy51/CommonSignals"},
	"smithed.custom_block": {"version":[0, 3, 0], "name":"Smithed Custom Block Placement", "url":"https://wiki.smithed.dev/libraries/custom-block/"},
	"smithed.crafter": {"version":[0, 3, 1], "name":"Smithed Crafter", "url":"https://wiki.smithed.dev/libraries/crafter/"},
	# "smart_ore_generation": {"version":[2, 0, 0], "name":"Stoupy's Smart Ore Generation", "url":"https://github.com/Stoupy51/SmartOreGeneration"},
	# "energy": {"version":[0, 6, 0], "name":"DatapackEnergy", "url":"https://github.com/ICY105/DatapackEnergy"},
	# "furnace_nbt_recipes": {"version":[2, 0, 0], "name":"Stoupy's Furnace NBT Recipes", "url":"https://github.com/Stoupy51/FurnaceNbtRecipes"},
}

# Technical constants
BUILD_DATAPACK: str = f"{BUILD_FOLDER}/datapack"									# Folder where the final datapack will be built
DATAPACK_FUNCTIONS: str = f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions"			# Folder where the datapack functions are built
BUILD_RESOURCE_PACK: str = f"{BUILD_FOLDER}/resource_pack"							# Folder where the final resource pack will be built
SOURCE_LORE: str = f'[{{"text":"{DATAPACK_NAME}","italic":true,"color":"blue"}}]'	# Appended lore to any custom item, can be an empty string
FACES: tuple = ("down", "up", "north", "south", "west", "east")						# Faces of a block, used for resource pack and blocks orientation
SIDES: tuple = ("_bottom", "_top", "_front", "_back", "_left", "_right", "_side")	# Sides of a block, used for resource pack
CUSTOM_BLOCK_VANILLA: str = "minecraft:furnace"			# Vanilla block used as base for custom blocks, must have the "facing" blockstate
CUSTOM_BLOCK_ALTERNATIVE: str = "minecraft:item_frame"		# Same purpose as previous, but useful for blocks that can be placed on walls or on player's position (ex: flowers)
CUSTOM_ITEM_VANILLA: str = "minecraft:command_block"	# Vanilla item used as base for custom items, must not have any survival vanilla behaviour
MODEL_DISPLAY: dict[str, dict] = {"head":{"rotation":[0,0,0],"translation":[0,-30.42,0],"scale":[1.605,1.605,1.605]},"fixed":{"rotation":[-90,0,0],"translation":[0,0,-16],"scale":[2.0075,2.0075,2.0075]}}	# Model display base for custom blocks
MAX_ITEMS_PER_ROW: int = 5		# Max number of items per row in the manual, should not exceed 6
MAX_ROWS_PER_PAGE: int = 5		# Max number of rows per page in the manual, should not exceed 6
OPENGL_RESOLUTION: int = 64		# Resolution of the OpenGL renders used in the manual, best value is 64 <--- 64x64

# UUIDs for attribute modifiers to avoid conflicts, feel free to use them for your database
UUIDS = {
	"attack_damage":		{"helmet": [0,1,2,3], "chestplate": [0,4,5,6], "leggings": [0,7,8,9], "boots": [0,10,11,12], "sword": [0,13,14,15], "pickaxe": [0,16,17,18], "axe": [0,19,20,21], "shovel": [0,22,23,24], "hoe": [0,25,26,27]},
	"attack_speed":			{"helmet": [1,1,2,3], "chestplate": [1,4,5,6], "leggings": [1,7,8,9], "boots": [1,10,11,12], "sword": [1,13,14,15], "pickaxe": [1,16,17,18], "axe": [1,19,20,21], "shovel": [1,22,23,24], "hoe": [1,25,26,27]},
	"armor":				{"helmet": [2,1,2,3], "chestplate": [2,4,5,6], "leggings": [2,7,8,9], "boots": [2,10,11,12], "sword": [2,13,14,15], "pickaxe": [2,16,17,18], "axe": [2,19,20,21], "shovel": [2,22,23,24], "hoe": [2,25,26,27]},
	"armor_toughness":		{"helmet": [3,1,2,3], "chestplate": [3,4,5,6], "leggings": [3,7,8,9], "boots": [3,10,11,12], "sword": [3,13,14,15], "pickaxe": [3,16,17,18], "axe": [3,19,20,21], "shovel": [3,22,23,24], "hoe": [3,25,26,27]},
	"knockback_resistance":	{"helmet": [4,1,2,3], "chestplate": [4,4,5,6], "leggings": [4,7,8,9], "boots": [4,10,11,12], "sword": [4,13,14,15], "pickaxe": [4,16,17,18], "axe": [4,19,20,21], "shovel": [4,22,23,24], "hoe": [4,25,26,27]},
	"luck":					{"helmet": [5,1,2,3], "chestplate": [5,4,5,6], "leggings": [5,7,8,9], "boots": [5,10,11,12], "sword": [5,13,14,15], "pickaxe": [5,16,17,18], "axe": [5,19,20,21], "shovel": [5,22,23,24], "hoe": [5,25,26,27]},
	"mining_speed":			{"helmet": [6,1,2,3], "chestplate": [6,4,5,6], "leggings": [6,7,8,9], "boots": [6,10,11,12], "sword": [6,13,14,15], "pickaxe": [6,16,17,18], "axe": [6,19,20,21], "shovel": [6,22,23,24], "hoe": [6,25,26,27]},
	"gravity":				{"helmet": [7,1,2,3], "chestplate": [7,4,5,6], "leggings": [7,7,8,9], "boots": [7,10,11,12], "sword": [7,13,14,15], "pickaxe": [7,16,17,18], "axe": [7,19,20,21], "shovel": [7,22,23,24], "hoe": [7,25,26,27]},
}

# Databases
RESULT_OF_CRAFTING: str = "result_of_crafting"			# Key to a list of recipes to craft the item, ex: "adamantium": {RESULT_OF_CRAFTING: [...]}
USED_FOR_CRAFTING: str = "used_for_crafting"			# Should not be used unless you are crafting a vanilla item (ex: iyc.chainmail -> chainmail armor)
CATEGORY: str = "category"								# Key for the category, used for recipes and the manual, ex: CATEGORY:"material" or CATEGORY:"equipment"
COMMANDS_ON_PLACEMENT: str = "commands_on_placement"	# Key to a list of commands to execute when a custom block is placed, should be a list of strings or a single string (with break lines if multiple commands)
COMMANDS_ON_BREAK: str = "commands_on_break"			# Key to a list of commands to execute when a custom block is broken, should be a list of strings or a single string (with break lines if multiple commands)
VANILLA_BLOCK: str = "vanilla_block"					# Key to a vanilla block that will be placed for custom block interaction, value can either a string of a dict {"id":"minecraft:chest", "block_states": ["facing", "type=single", "waterlogged=false"]}
VANILLA_BLOCK_FOR_ORES: str = "minecraft:polished_deepslate"	# Vanilla block that will be used for an optimization tip for ores, don't ask questions
NO_SILK_TOUCH_DROP: str = "no_silk_touch_drop"			# Key to an item ID that will drop when silk touch is not used. Must be used only when using the vanilla block for ores, ex: "adamantium_fragment" or "minecraft:raw_iron"
NOT_COMPONENTS: list[str] = [							# Keys that should not be considered as components. Used for recipes, loot tables, etc.
	"id", "wiki", CATEGORY, RESULT_OF_CRAFTING,
	USED_FOR_CRAFTING, VANILLA_BLOCK,
	NO_SILK_TOUCH_DROP, COMMANDS_ON_PLACEMENT,
	COMMANDS_ON_BREAK]
DATABASE: dict[str, dict] = {}				# Dictionnary containing all the items, blocks, recipes, etc. used by the program. See format in database/README.md
EXTERNAL_DATABASE: dict[str, dict] = {}		# Should be filled when you require an item from another datapack for a recipe or anything else

