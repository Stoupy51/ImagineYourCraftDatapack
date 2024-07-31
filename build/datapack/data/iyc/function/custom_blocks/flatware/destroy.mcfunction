
#> iyc:custom_blocks/flatware/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_structure_void
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:structure_void"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/flatware/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_structure_void iyc.data 1
scoreboard players remove #total_flatware iyc.data 1

# Kill the custom block entity
kill @s

