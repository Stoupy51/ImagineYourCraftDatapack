
# Import config
from src.config import *
from src.utils.io import *
from src.utils.print import *

# For each custom block
unique_blocks = set()
for item, data in DATABASE.items():

	# Custom block
	if data.get(VANILLA_BLOCK):
		block = data[VANILLA_BLOCK]
		path = f"{DATAPACK_FUNCTIONS}/custom_blocks/{item}"

		## Place function	
		# Place block
		if isinstance(block, str):
			content = f"setblock ~ ~ ~ {block}\n"
		else:

			# Handle block states
			content = ""
			states = block.get("block_states")
			states = [] if not states else states
			block = block["id"]
			if "facing" in states:
				other_states = [state for state in states if state != "facing"]

				# For each face, make a different setblock depending on the vanilla block facing
				for face in FACES[2:]:
					content += f"execute if block ~ ~ ~ {CUSTOM_BLOCK_VANILLA}[facing={face}] run setblock ~ ~ ~ {block}[facing={face}"

					# Add the other states to the block
					for state in other_states:
						content += f",{state}"
					content += "]\n"
			else:
				# Simple setblock with all block states
				content += f"setblock ~ ~ ~ {block}[" + ",".join(states) + "]\n"
		
		# Summon item display and call secondary function
		content += f"execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function {NAMESPACE}:custom_blocks/{item}/place_secondary\n"
		write_to_file(f"{path}/place_main.mcfunction", content)

		## Secondary function
		unique_blocks.add(block)
		block = block.replace(":","_")
		custom_model_data = data["custom_model_data"]
		content = f"""
# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add {NAMESPACE}.custom_block
tag @s add {NAMESPACE}.{item}
tag @s add {NAMESPACE}.vanilla.{block}

# Modify item display entity to match the custom block
item replace entity @s container.0 with deepslate[minecraft:custom_model_data={custom_model_data}]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
data modify entity @s brightness set value {{block:15,sky:15}}

## Check if the block have rotation
# Furnace case
scoreboard players set #rotation {NAMESPACE}.data 0
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ furnace[facing=north] run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ furnace[facing=east] run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ furnace[facing=south] run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ furnace[facing=west] run data modify entity @s Rotation[0] set value 90.0f
# Iron trapdoor case
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ iron_trapdoor[facing=north] run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ iron_trapdoor[facing=east] run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ iron_trapdoor[facing=south] run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation {NAMESPACE}.data matches 0 store success score #rotation {NAMESPACE}.data if block ~ ~ ~ iron_trapdoor[facing=west] run data modify entity @s Rotation[0] set value 90.0f
# No more cases for now

"""
		# Add the commands on placement if any
		if COMMANDS_ON_PLACEMENT in data:
			if isinstance(data[COMMANDS_ON_PLACEMENT], list):
				content += "\n".join(data[COMMANDS_ON_PLACEMENT]) + "\n"
			else:
				content += f"{data[COMMANDS_ON_PLACEMENT]}\n"
			
		# Write file
		write_to_file(f"{path}/place_secondary.mcfunction", content)
	pass



## Destroy functions
# For each unique block, if the vanilla block is missing, call the destroy function for the group
content = "\n"
for block in unique_blocks:
	block_underscore = block.replace(":","_")
	content += f"execute if entity @s[tag={NAMESPACE}.vanilla.{block_underscore}] unless block ~ ~ ~ {block} run function {NAMESPACE}:custom_blocks/_groups/{block_underscore}\n"
write_to_file(f"{DATAPACK_FUNCTIONS}/custom_blocks/destroy.mcfunction", content + "\n")

# For each unique block, make the group function
for block in unique_blocks:
	block_underscore = block.replace(":","_")
	content = "\n"

	# For every custom block, add a tag check for destroy if it's the right vanilla block
	for item, data in DATABASE.items():
		if data.get(VANILLA_BLOCK):

			# Get the vanilla block
			this_block = data[VANILLA_BLOCK]
			if isinstance(this_block, dict):
				this_block = this_block["id"]
			this_block = this_block.replace(":","_")

			# Add the line if it's the same vanilla block
			if this_block == block_underscore:
				content += f"execute if entity @s[tag={NAMESPACE}.{item}] run function {NAMESPACE}:custom_blocks/{item}/destroy\n"
	write_to_file(f"{DATAPACK_FUNCTIONS}/custom_blocks/_groups/{block_underscore}.mcfunction", content + "\n")

# For each custom block, make it's destroy function
for item, data in DATABASE.items():
	if data.get(VANILLA_BLOCK):
		block = data[VANILLA_BLOCK]
		path = f"{DATAPACK_FUNCTIONS}/custom_blocks/{item}"
		if isinstance(block, dict):
			block = block["id"]
		
		# Destroy function
		content = f"""
# Kill undesired items and replace the item
data modify entity @e[type=item,nbt={{Item:{{id:"{block}"}}}},limit=1,sort=nearest,distance=..1] Item.components set from storage {NAMESPACE}:items all.{item}.components
data modify entity @e[type=item,nbt={{Item:{{id:"{block}"}}}},limit=1,sort=nearest,distance=..1] Item.id set from storage {NAMESPACE}:items all.{item}.id
"""
		# Add the commands on break if any
		if COMMANDS_ON_BREAK in data:
			if isinstance(data[COMMANDS_ON_BREAK], list):
				content += "\n".join(data[COMMANDS_ON_BREAK]) + "\n"
			else:
				content += f"{data[COMMANDS_ON_BREAK]}\n"
		
		# Write file
		write_to_file(f"{path}/destroy.mcfunction", content + "kill @s\n\n")


# Write the used_vanilla_blocks tag, the predicate to check the blocks with the tag and an advanced one
VANILLA_BLOCKS_TAG = "used_vanilla_blocks"
write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/blocks/{VANILLA_BLOCKS_TAG}.json", super_json_dump({"values": list(unique_blocks)}))
predicate = {"condition": "minecraft:location_check", "predicate": {"block": {"blocks": f"#{NAMESPACE}:{VANILLA_BLOCKS_TAG}"}}}
write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/predicates/check_vanilla_blocks.json", super_json_dump(predicate))
advanced_predicate = {"condition": "minecraft:any_of", "terms": []}
for block in unique_blocks:
	block_underscore = block.replace(":","_")
	predicate = {"condition": "minecraft:entity_properties", "entity": "this", "predicate": { "nbt": f"{{Tags:[\"iyc.vanilla.{block_underscore}\"]}}", "location": { "block": { "blocks": [block] }}}}
	advanced_predicate["terms"].append(predicate)
write_to_file(f"{BUILD_DATAPACK}/data/{NAMESPACE}/predicates/advanced_check_vanilla_blocks.json", super_json_dump(advanced_predicate))

# Write a destroy check every 2 ticks, every second, and every 5 seconds
write_to_file(f"{DATAPACK_FUNCTIONS}/tick_2.mcfunction", f"""
# 2 ticks destroy detection
execute as @e[type=item_display,tag={NAMESPACE}.custom_block,tag=!{NAMESPACE}.vanilla.{VANILLA_BLOCK_FOR_ORES.replace(':', '_')},predicate=!{NAMESPACE}:check_vanilla_blocks] at @s run function {NAMESPACE}:custom_blocks/destroy
""")
write_to_file(f"{DATAPACK_FUNCTIONS}/second.mcfunction", f"""
# 1 second break detection
execute as @e[type=item_display,tag={NAMESPACE}.custom_block,tag=!{NAMESPACE}.vanilla.{VANILLA_BLOCK_FOR_ORES.replace(':', '_')},predicate=!{NAMESPACE}:advanced_check_vanilla_blocks] at @s run function {NAMESPACE}:custom_blocks/destroy
""")
write_to_file(f"{DATAPACK_FUNCTIONS}/second_5.mcfunction", f"""
# 5 seconds break detection
execute as @e[type=item_display,tag={NAMESPACE}.custom_block,predicate=!{NAMESPACE}:advanced_check_vanilla_blocks] at @s run function {NAMESPACE}:custom_blocks/destroy
""")



info("All customs blocks are now placeable and destroyable!")

