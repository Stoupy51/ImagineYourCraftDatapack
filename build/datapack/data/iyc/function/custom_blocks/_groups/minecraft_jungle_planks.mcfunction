
#> iyc:custom_blocks/_groups/minecraft_jungle_planks
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_reversed_jungle_planks iyc.data matches 1.. if entity @s[tag=iyc.reversed_jungle_planks] run function iyc:custom_blocks/reversed_jungle_planks/destroy

