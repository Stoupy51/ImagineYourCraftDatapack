
#> iyc:custom_blocks/_groups/minecraft_dark_oak_planks
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_reversed_dark_oak_planks iyc.data matches 1.. if entity @s[tag=iyc.reversed_dark_oak_planks] run function iyc:custom_blocks/reversed_dark_oak_planks/destroy

