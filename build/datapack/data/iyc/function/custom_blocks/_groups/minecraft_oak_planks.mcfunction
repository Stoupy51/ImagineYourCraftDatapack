
#> iyc:custom_blocks/_groups/minecraft_oak_planks
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_box_jump iyc.data matches 1.. if entity @s[tag=iyc.box_jump] run function iyc:custom_blocks/box_jump/destroy
execute if score #total_box_speed iyc.data matches 1.. if entity @s[tag=iyc.box_speed] run function iyc:custom_blocks/box_speed/destroy
execute if score #total_reversed_oak_planks iyc.data matches 1.. if entity @s[tag=iyc.reversed_oak_planks] run function iyc:custom_blocks/reversed_oak_planks/destroy

