
#> iyc:custom_blocks/log_fence_gate/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_oak_fence_gate
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:oak_fence_gate"}},distance=..1] run function iyc:custom_blocks/log_fence_gate/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_oak_fence_gate iyc.data 1
scoreboard players remove #total_log_fence_gate iyc.data 1

# Kill the custom block entity
kill @s

