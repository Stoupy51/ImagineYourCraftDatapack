
# Import config
from src.importer import *

# Setup load json files and tick json file
with super_open(f"{BUILD_DATAPACK}/data/load/tags/functions/load.json", "w") as f:
	f.write(super_json_dump({"values": [f"#{NAMESPACE}:load/main"]}) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/main.json", "w") as f:
	f.write(super_json_dump({"values": [{"id":f"#{NAMESPACE}:load/dependencies","required":False}, f"{NAMESPACE}:load/main"]}, max_level = 3) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/functions/load/dependencies.json", "w") as f:
	f.write(super_json_dump({"values": []}) + "\n")
with super_open(f"{BUILD_DATAPACK}/data/minecraft/tags/functions/tick.json", "w") as f:
	f.write(super_json_dump({"values": [f"{NAMESPACE}:load/tick_verification"]}) + "\n")
	pass

# Setup load main function
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/main.mcfunction", "w") as f:
	f.write(f"""
# Avoiding multiple executions of the same load function
execute unless score {DATAPACK_NAME} load.status matches 1.. run function {NAMESPACE}:load/secondary
""" + "\n")
	pass
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/load/secondary.mcfunction", "w") as f:
	f.write(f"""
# {DATAPACK_NAME}
scoreboard objectives add {NAMESPACE}.data dummy
scoreboard players set {NAMESPACE} load.status {int(SCORE_VERSION)}
tag {AUTHOR} add convention.debug

# Check dependencies and wait for a player to connect (to get server version)
function {NAMESPACE}:load/check_dependencies
function {NAMESPACE}:load/waiting_for_player
""" + "\n")

"""
## Check if SimplEnergy is loadable (dependencies)
scoreboard players set #load_error simplenergy.data 0
execute if score #load_error simplenergy.data matches 0 unless score #smithed.custom_block.major load.status matches 0.. run scoreboard players set #load_error simplenergy.data 2
execute if score #load_error simplenergy.data matches 0 unless score #smithed.crafter.major load.status matches 0.. run scoreboard players set #load_error simplenergy.data 2
execute if score #load_error simplenergy.data matches 0 unless score #energy.minor load.status matches 6.. run scoreboard players set #load_error simplenergy.data 2
execute if score #load_error simplenergy.data matches 0 unless score SmartOreGeneration load.status matches 11.. run scoreboard players set #load_error simplenergy.data 2
execute if score #load_error simplenergy.data matches 0 unless score DurabilityMultiplier load.status matches 13.. run scoreboard players set #load_error simplenergy.data 2
execute if score #load_error simplenergy.data matches 0 unless score FurnaceNbtRecipes load.status matches 11.. run scoreboard players set #load_error simplenergy.data 2

"""
# TODO : check_dependencies and waiting_for_player

