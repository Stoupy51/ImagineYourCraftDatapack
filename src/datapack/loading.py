
# Import config
from src.importer import *

# Setup load json files and tick json file
with super_open(f"{BUILD_DATAPACK}/data/load/tags/functions/load.json", "w") as f:
	f.write(super_json_dump({"values": [f"#{NAMESPACE}:load/main"]}))
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/main.json", "w") as f:
	f.write(super_json_dump({"values": [{"id":f"#{NAMESPACE}:load/dependencies","required":False}, f"{NAMESPACE}:load/main"]}, max_level = 3))
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/dependencies.json", "w") as f:
	calls = [{"id":f"#{namespace}:load", "required": False} for namespace in DEPENDENCIES.keys()]
	f.write(super_json_dump({"values": calls}))
with super_open(f"{BUILD_DATAPACK}/data/minecraft/tags/functions/tick.json", "w") as f:
	f.write(super_json_dump({"values": [f"{NAMESPACE}:load/tick_verification"]}))
	pass


# Setup load main and secondary function
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/main.mcfunction", "w") as f:
	f.write(f"""
# Avoiding multiple executions of the same load function
execute unless score {DATAPACK_NAME} load.status matches 1.. run function {NAMESPACE}:load/secondary

""")
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/secondary.mcfunction", "w") as f:
	major, minor, patch = VERSION.split(".")
	f.write(f"""
# {DATAPACK_NAME}
scoreboard objectives add {NAMESPACE}.data dummy
scoreboard players set #{NAMESPACE}.major load.status {major}
scoreboard players set #{NAMESPACE}.minor load.status {minor}
scoreboard players set #{NAMESPACE}.patch load.status {patch}
tag {AUTHOR} add convention.debug

# Check dependencies and wait for a player to connect (to get server version)
function {NAMESPACE}:load/check_dependencies
function {NAMESPACE}:load/waiting_for_player

""")
	pass


# Check Dependencies
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/check_dependencies.mcfunction", "w") as f:
	checks = ""
	for namespace, value in DEPENDENCIES.items():
		major, minor, patch = value["version"]
		checks += f"execute if score #load_error {NAMESPACE}.data matches 0 unless score #{namespace}.major load.status matches {major}.. unless score #{namespace}.minor load.status matches {minor}.. unless score #{namespace}.patch load.status matches {patch}.. run scoreboard players set #load_error {NAMESPACE}.data 1\n"
	f.write(f"""
## Check if {DATAPACK_NAME} is loadable (dependencies)
scoreboard players set #load_error {NAMESPACE}.data 0
{checks}
""")
	pass


# Waiting for player
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/waiting_for_player.mcfunction", "w") as f:
	decoder_checks = ""
	for namespace, value in DEPENDENCIES.items():
		major, minor, patch = value["version"]
		name = value["name"]
		url = value["url"]
		decoder_checks += f'execute if score #load_error {NAMESPACE}.data matches 1 unless score #{namespace}.major load.status matches {major}.. unless score #{namespace}.minor load.status matches {minor}.. unless score #{namespace}.patch load.status matches {patch}.. run tellraw @a {{"text":"- [{name}]","color":"gold","clickEvent":{{"action":"open_url","value":"{url}"}}}}\n'
	f.write(f"""
# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run schedule function {NAMESPACE}:load/waiting_for_player 1t replace
execute unless entity @p run return 0
execute store result score #{NAMESPACE}.game_version {NAMESPACE}.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error {NAMESPACE}.data 0
execute unless score #game_version {NAMESPACE}.data matches {DATA_VERSION}.. run scoreboard players set #mcload_error {NAMESPACE}.data 1

# Decode errors
execute if score #mcload_error {NAMESPACE}.data matches 1 run tellraw @a {{"text":"{DATAPACK_NAME} Error: This version is made for Minecraft {MINECRAFT_VERSION}+.","color":"red"}}
execute if score #mcload_error {NAMESPACE}.data matches 2 run tellraw @a {{"text":"{DATAPACK_NAME} Error: Libraries are missing\nplease download the right {DATAPACK_NAME} datapack\nor download each of these libraries one by one:","color":"red"}}
{decoder_checks}

# Load {DATAPACK_NAME}
execute if score #game_version {NAMESPACE}.data matches 1.. if score #mcload_error {NAMESPACE}.data matches 0 if score #load_error {NAMESPACE}.data matches 0 run function {NAMESPACE}:load/confirm_load

""")
	pass

# TODO: confirm load




