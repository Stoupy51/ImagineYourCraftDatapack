
#> iyc:custom_blocks/_groups/minecraft_cherry_planks
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_reversed_cherry_planks iyc.data matches 1.. if entity @s[tag=iyc.reversed_cherry_planks] run function iyc:custom_blocks/reversed_cherry_planks/destroy

