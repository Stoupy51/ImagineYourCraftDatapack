
#> iyc:custom_blocks/_groups/minecraft_stone_pressure_plate
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_glowstone_pressure_plate iyc.data matches 1.. if entity @s[tag=iyc.glowstone_pressure_plate] run function iyc:custom_blocks/glowstone_pressure_plate/destroy

