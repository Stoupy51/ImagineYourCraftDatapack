
# Import config
from src.importer import *

# Setup load json files and tick json file
with super_open(f"{BUILD_DATAPACK}/data/load/tags/functions/load.json", "w") as f:
	f.write(super_json_dump({"values": [f"#{NAMESPACE}:load/main"]}) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/main.json", "w") as f:
	f.write(super_json_dump({"values": [{"id":f"#{NAMESPACE}:load/dependencies","required":False}, f"{NAMESPACE}:load/main"]}, max_level = 3) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/dependencies.json", "w") as f:
	calls = [{"id":f"#{namespace}:load", "required": False} for namespace in DEPENDENCIES]
	f.write(super_json_dump({"values": calls}) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/minecraft/tags/functions/tick.json", "w") as f:
	f.write(super_json_dump({"values": [f"{NAMESPACE}:load/tick_verification"]}) + "\n")
	pass

# Setup load main and secondary function
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/main.mcfunction", "w") as f:
	f.write(f"""
# Avoiding multiple executions of the same load function
execute unless score {DATAPACK_NAME} load.status matches 1.. run function {NAMESPACE}:load/secondary
""" + "\n")
	pass
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
""" + "\n")
	pass

# Check Dependencies
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/check_dependencies.mcfunction", "w") as f:
	checks = ""
	for namespace, version in DEPENDENCIES.items():
		major, minor, patch = version
		checks += f"execute if score #load_error {NAMESPACE}.data matches 0 unless score #{namespace}.major load.status matches {major}.. unless score #{namespace}.minor load.status matches {minor}.. unless score #{namespace}.patch load.status matches {patch}.. run scoreboard players set #load_error {NAMESPACE}.data 1\n"
	f.write(f"""
## Check if {DATAPACK_NAME} is loadable (dependencies)
scoreboard players set #load_error {NAMESPACE}.data 0
{checks}""" + "\n")
	pass

# Waiting for player


