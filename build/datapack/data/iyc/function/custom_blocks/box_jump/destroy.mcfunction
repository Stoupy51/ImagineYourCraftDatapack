
#> iyc:custom_blocks/box_jump/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_oak_planks
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:oak_planks"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/box_jump/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_oak_planks iyc.data 1
scoreboard players remove #total_box_jump iyc.data 1

# Kill the custom block entity
kill @s

