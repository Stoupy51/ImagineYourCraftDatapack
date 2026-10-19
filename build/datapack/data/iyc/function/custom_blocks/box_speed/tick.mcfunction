
#> iyc:custom_blocks/box_speed/tick
#
# @executed	as @e[tag=iyc.tick] & at @s
#
# @within	iyc:custom_blocks/tick
#

execute positioned ~-0.5 ~0.5 ~-0.5 as @a[dx=0,dy=0,dz=0,gamemode=!spectator] run effect give @s minecraft:speed 1 2 true

