
#> iyc:custom_blocks/reversed_cherry_planks/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_cherry_planks
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:cherry_planks"}},distance=..1] run function iyc:custom_blocks/reversed_cherry_planks/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_cherry_planks iyc.data 1
scoreboard players remove #total_reversed_cherry_planks iyc.data 1

# Kill the custom block entity
kill @s

