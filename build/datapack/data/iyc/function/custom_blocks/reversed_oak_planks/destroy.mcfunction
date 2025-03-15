
#> iyc:custom_blocks/reversed_oak_planks/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_oak_planks
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:oak_planks"}},distance=..1] run function iyc:custom_blocks/reversed_oak_planks/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_oak_planks iyc.data 1
scoreboard players remove #total_reversed_oak_planks iyc.data 1

# Kill the custom block entity
kill @s

