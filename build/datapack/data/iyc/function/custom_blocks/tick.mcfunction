
#> iyc:custom_blocks/tick
#
# @executed	as @e[tag=iyc.tick] & at @s
#
# @within	iyc:v0.1.0/tick [ as @e[tag=iyc.tick] & at @s ]
#

execute if entity @s[tag=iyc.box_jump] run function iyc:custom_blocks/box_jump/tick
execute if entity @s[tag=iyc.box_speed] run function iyc:custom_blocks/box_speed/tick
execute if entity @s[tag=iyc.iron_furnace] run function iyc:custom_blocks/iron_furnace/tick
execute if entity @s[tag=iyc.steel_brewing_stand] run function iyc:custom_blocks/steel_brewing_stand/tick

