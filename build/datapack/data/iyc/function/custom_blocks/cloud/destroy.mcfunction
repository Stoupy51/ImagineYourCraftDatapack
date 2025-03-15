
#> iyc:custom_blocks/cloud/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_structure_void
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1] run function iyc:custom_blocks/cloud/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_structure_void iyc.data 1
scoreboard players remove #total_cloud iyc.data 1

# Kill the custom block entity
kill @s

