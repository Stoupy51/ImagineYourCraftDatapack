
#> iyc:custom_blocks/iron_ladder/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_ladder
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:ladder"}},distance=..1] run function iyc:custom_blocks/iron_ladder/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_ladder iyc.data 1
scoreboard players remove #total_iron_ladder iyc.data 1

# Kill the custom block entity
kill @s

