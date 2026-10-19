
#> iyc:custom_blocks/box_jump/tick
#
# @executed	as @e[tag=iyc.tick] & at @s
#
# @within	iyc:custom_blocks/tick
#

execute positioned ~-0.5 ~0.5 ~-0.5 as @a[dx=0,dy=0,dz=0,tag=!iyc.launched,gamemode=!spectator] run function iyc:jump_box/launch
execute positioned ~-0.5 ~0.5 ~-0.5 as @e[type=!player,type=!#iyc:not_living,dx=0,dy=0,dz=0] run data modify entity @s Motion[1] set value 4.0d

