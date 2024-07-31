
#> iyc:custom_blocks/cherry_cake/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_cake
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:cake"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/cherry_cake/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_cake iyc.data 1
scoreboard players remove #total_cherry_cake iyc.data 1

# Kill the custom block entity
kill @s

