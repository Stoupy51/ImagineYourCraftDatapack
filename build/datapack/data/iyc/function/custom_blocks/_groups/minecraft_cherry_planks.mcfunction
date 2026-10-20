
#> iyc:custom_blocks/_groups/minecraft_cherry_planks
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_reversed_cherry_planks iyc.data matches 1.. if entity @s[tag=iyc.reversed_cherry_planks] run function iyc:custom_blocks/reversed_cherry_planks/destroy

