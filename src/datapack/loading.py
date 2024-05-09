
# Import config
from config import *
from src.utils.io import *
from src.utils.print import *


# Setup load json files and tick json file
write_to_file(f"{BUILD_DATAPACK}/data/load/tags/functions/load.json", super_json_dump({"values": [f"#{NAMESPACE}:load/main"]}))
write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/main.json", super_json_dump({"values": [{"id":f"#{NAMESPACE}:load/dependencies","required":False}, f"{NAMESPACE}:load/main"]}, max_level = 3))
calls = [{"id":f"#{namespace}:load", "required": False} for namespace in DEPENDENCIES.keys()]
write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/dependencies.json", super_json_dump({"values": calls}))
write_to_file(f"{BUILD_DATAPACK}/data/minecraft/tags/functions/tick.json", super_json_dump({"values": [f"{NAMESPACE}:load/tick_verification"]}))


# Setup load main and secondary function
write_to_file(f"{DATAPACK_FUNCTIONS}/load/main.mcfunction", f"""
# Avoiding multiple executions of the same load function
execute unless score {DATAPACK_NAME_SIMPLE} load.status matches 1.. run function {NAMESPACE}:load/secondary

""")
major, minor, patch = VERSION.split(".")
authors = AUTHOR.split(" ")
convention_debug = "".join([f"tag {author} add convention.debug\n" for author in authors])
content = f"""
# {DATAPACK_NAME}
scoreboard objectives add {NAMESPACE}.data dummy
scoreboard players set #{NAMESPACE}.major load.status {major}
scoreboard players set #{NAMESPACE}.minor load.status {minor}
scoreboard players set #{NAMESPACE}.patch load.status {patch}
{convention_debug}

# Check dependencies and wait for a player to connect (to get server version)
function {NAMESPACE}:load/check_dependencies
function {NAMESPACE}:load/waiting_for_player

"""
write_to_file(f"{DATAPACK_FUNCTIONS}/load/secondary.mcfunction", content)


# Check dependencies
checks = ""
for namespace, value in DEPENDENCIES.items():
	major, minor, patch = value["version"]
	checks += f"execute if score #dependency_error {NAMESPACE}.data matches 0 unless score #{namespace}.major load.status matches {major}.. unless score #{namespace}.minor load.status matches {minor}.. unless score #{namespace}.patch load.status matches {patch}.. run scoreboard players set #dependency_error {NAMESPACE}.data 1\n"
content = f"""
## Check if {DATAPACK_NAME} is loadable (dependencies)
scoreboard players set #dependency_error {NAMESPACE}.data 0"""
content += "\n" + checks + "\n"
write_to_file(f"{DATAPACK_FUNCTIONS}/load/check_dependencies.mcfunction", content)


# Waiting for player
decoder_checks = ""
for namespace, value in DEPENDENCIES.items():
	major, minor, patch = value["version"]
	name = value["name"]
	url = value["url"]
	decoder_checks += f'execute if score #dependency_error {NAMESPACE}.data matches 1 unless score #{namespace}.major load.status matches {major}.. unless score #{namespace}.minor load.status matches {minor}.. unless score #{namespace}.patch load.status matches {patch}.. run tellraw @a {{"text":"- [{name}]","color":"gold","clickEvent":{{"action":"open_url","value":"{url}"}}}}\n'
write_to_file(f"{DATAPACK_FUNCTIONS}/load/waiting_for_player.mcfunction", f"""
# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run schedule function {NAMESPACE}:load/waiting_for_player 1t replace
execute unless entity @p run return 0
execute store result score #game_version {NAMESPACE}.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error {NAMESPACE}.data 0
execute unless score #game_version {NAMESPACE}.data matches {DATA_VERSION}.. run scoreboard players set #mcload_error {NAMESPACE}.data 1

# Decode errors
execute if score #mcload_error {NAMESPACE}.data matches 1 run tellraw @a {{"text":"{DATAPACK_NAME} Error: This version is made for Minecraft {MINECRAFT_VERSION}+.","color":"red"}}
execute if score #dependency_error {NAMESPACE}.data matches 1 run tellraw @a {{"text":"{DATAPACK_NAME} Error: Libraries are missing\\nplease download the right {DATAPACK_NAME} datapack\\nor download each of these libraries one by one:","color":"red"}}
{decoder_checks}
# Load {DATAPACK_NAME}
execute if score #game_version {NAMESPACE}.data matches 1.. if score #mcload_error {NAMESPACE}.data matches 0 if score #dependency_error {NAMESPACE}.data matches 0 run function {NAMESPACE}:load/confirm_load

""")


# Confirm load
items_storage = ""	# Storage representation of every item in the database
content = ""
for item, data in DATABASE.items():
	mc_data = {"id":"","count":1, "components":{"custom_model_data":-1}}
	for k, v in data.items():
		if k not in NOT_COMPONENTS:
			mc_data["components"][k] = v
		elif k == "id":
			mc_data[k] = v
	items_storage += f"data modify storage {NAMESPACE}:items all.{item} set value " + super_json_dump(mc_data, max_level = 0)
	pass

write_to_file(f"{DATAPACK_FUNCTIONS}/load/confirm_load.mcfunction", f"""
tellraw @a[tag=convention.debug] {{"text":"[Loaded {DATAPACK_NAME} v{VERSION}]","color":"green"}}

scoreboard objectives add {NAMESPACE}.private dummy
scoreboard objectives add {NAMESPACE}.right_click minecraft.used:minecraft.warped_fungus_on_a_stick

scoreboard players set #{NAMESPACE}.loaded load.status 1
# "#second" starts at a random time for better load distribution
execute store result score #second {NAMESPACE}.data run random value 1..19

# Items storage
data modify storage {NAMESPACE}:items all set value {{}}
{items_storage}
""")


# Tick verification
write_to_file(f"{DATAPACK_FUNCTIONS}/load/tick_verification.mcfunction", f"""
execute if score #{NAMESPACE}.loaded load.status matches 1 run function {NAMESPACE}:tick

""")
info("All loading functions and tags created")

