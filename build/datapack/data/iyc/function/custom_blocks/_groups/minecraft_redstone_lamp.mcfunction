
#> iyc:custom_blocks/_groups/minecraft_redstone_lamp
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_red_light iyc.data matches 1.. if entity @s[tag=iyc.red_light] run function iyc:custom_blocks/red_light/destroy

