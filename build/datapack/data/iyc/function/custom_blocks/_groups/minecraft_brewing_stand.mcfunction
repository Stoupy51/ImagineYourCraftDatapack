
#> iyc:custom_blocks/_groups/minecraft_brewing_stand
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_steel_brewing_stand iyc.data matches 1.. if entity @s[tag=iyc.steel_brewing_stand] run function iyc:custom_blocks/steel_brewing_stand/destroy

