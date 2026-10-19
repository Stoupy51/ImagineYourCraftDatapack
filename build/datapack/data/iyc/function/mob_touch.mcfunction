
#> iyc:mob_touch
#
# @executed	as @e[type=!player] & at @s
#
# @within	iyc:v0.1.0/tick [ as @e[type=!player] & at @s ]
#

execute if block ~ ~ ~ minecraft:tripwire run return run function iyc:flowers/touch
execute if entity @e[type=item_display,tag=iyc.cloud,distance=..0.9] run data modify entity @s fall_distance set value 0.0d

