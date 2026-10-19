
#> iyc:custom_blocks/reversed_spruce_planks/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_spruce_planks
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:spruce_planks"}},distance=..1] run function iyc:custom_blocks/reversed_spruce_planks/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_spruce_planks iyc.data 1
scoreboard players remove #total_reversed_spruce_planks iyc.data 1

# Kill the custom block entity
kill @s

