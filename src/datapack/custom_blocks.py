
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
		path = f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/custom_blocks/{item}"

		# Place function
		with super_open(f"{path}/place_main.mcfunction", "w") as f:

			# Place block
			if isinstance(block, str):
				f.write(f"setblock ~ ~ ~ {block}\n")
			else:

				# Handle block states
				states = block["block_states"]
				block = block["id"]
				if "facing" in states:
					other_states = [state for state in states if state != "facing"]
					for face in FACES[2:]:
						f.write(f"execute if block ~ ~ ~ {CUSTOM_BLOCK_VANILLA}[facing={face}] run setblock ~ ~ ~ {block}[facing={face}")
						for state in other_states:
							f.write(f",{state}")
						f.write("]\n")
				else:
					f.write(f"setblock ~ ~ ~ {block}[" + ",".join(states) + "]\n")
			
			# Summon item display and call secondary function
			f.write(f"execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function {NAMESPACE}:custom_blocks/{item}/place_secondary\n")

		# Secondary function
		with super_open(f"{path}/place_secondary.mcfunction", "w") as f:
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
			f.write(content)
	pass



# Destroy functions
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/custom_blocks/destroy.mcfunction", "w") as f:
	content = "\n"
	for block in unique_blocks:
		block_underscore = block.replace(":","_")
		content += f"execute if entity @s[tag={NAMESPACE}.vanilla.{block_underscore}] unless block ~ ~ ~ {block} run function {NAMESPACE}:custom_blocks/_groups/{block_underscore}\n"
	f.write(content + "\n")
for block in unique_blocks:
	block_underscore = block.replace(":","_")
	with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/custom_blocks/_groups/{block_underscore}.mcfunction", "w") as f:
		content = "\n"
		for item, data in DATABASE.items():
			if data.get(VANILLA_BLOCK):

				# Get the vanilla block
				this_block = data[VANILLA_BLOCK]
				if isinstance(this_block, dict):
					this_block = this_block["id"]
				this_block = this_block.replace(":","_")

				# Add the call to the right function
				if this_block == block_underscore:
					content += f"execute if entity @s[tag={NAMESPACE}.{item}] run function {NAMESPACE}:custom_blocks/{item}/destroy\n"
		f.write(content + "\n")
for item, data in DATABASE.items():
	if data.get(VANILLA_BLOCK):
		block = data[VANILLA_BLOCK]
		path = f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/custom_blocks/{item}"
		if isinstance(block, dict):
			block = block["id"]
		
		# Destroy function
		with super_open(f"{path}/destroy.mcfunction", "w") as f:
			content = f"""
# Kill undesired items and replace the item
data modify entity @e[type=item,nbt={{Item:{{id:"{block}"}}}},limit=1,sort=nearest,distance=..1] Item.components set from storage {NAMESPACE}:items all.{item}.components
data modify entity @e[type=item,nbt={{Item:{{id:"{block}"}}}},limit=1,sort=nearest,distance=..1] Item.id set from storage {NAMESPACE}:items all.{item}.id
"""
			# Add the commands on destruction if any
			if COMMANDS_ON_BREAK in data:
				if isinstance(data[COMMANDS_ON_BREAK], list):
					content += "\n".join(data[COMMANDS_ON_BREAK]) + "\n"
				else:
					content += f"{data[COMMANDS_ON_BREAK]}\n"
			
			# Write file
			f.write(content + "kill @s\n\n")



# Write the used_vanilla_blocks tag, the predicate to check the blocks with the tag, and the tick_2 function to check the blocks
VANILLA_BLOCKS_TAG = "used_vanilla_blocks"
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/tags/blocks/{VANILLA_BLOCKS_TAG}.json", "w") as f:
	super_json_dump({"values": list(unique_blocks)}, f)
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/predicates/check_vanilla_blocks.json", "w") as f:
	predicate = {"condition": "minecraft:location_check", "predicate": {"block": {"blocks": f"#{NAMESPACE}:{VANILLA_BLOCKS_TAG}"}}}
	super_json_dump(predicate, f)
"""
# 2 ticks destroy detection
execute as @e[tag=simplenergy.destroyer,tag=!simplenergy.item_destroy,predicate=!simplenergy:check_destroyer] at @s run function simplenergy:destroy/all
"""
with super_open(f"{BUILD_DATAPACK}/data/{NAMESPACE}/functions/tick_2.mcfunction", "w") as f:
	f.write(f"""
# 2 ticks destroy detection
execute as @e[type=item_display,tag={NAMESPACE}.custom_block,tag=!{NAMESPACE}.vanilla.{VANILLA_BLOCK_FOR_ORES.replace(':', '')},predicate=!{NAMESPACE}:check_vanilla_blocks] at @s run function {NAMESPACE}:custom_blocks/destroy

""")




info("All customs blocks are now placeable and destroyable!")

