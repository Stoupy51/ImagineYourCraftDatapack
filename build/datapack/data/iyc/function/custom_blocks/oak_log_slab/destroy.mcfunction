
#> iyc:custom_blocks/oak_log_slab/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_oak_slab
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:oak_slab"}},distance=..1] run function iyc:custom_blocks/oak_log_slab/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_oak_slab iyc.data 1
scoreboard players remove #total_oak_log_slab iyc.data 1

# Kill the custom block entity
kill @s

