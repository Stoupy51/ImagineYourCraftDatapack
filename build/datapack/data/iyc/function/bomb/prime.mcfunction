
#> iyc:bomb/prime
#
# @executed	as @e[type=tnt,distance=..1,tag=!iyc.bomb]
#
# @within	iyc:custom_blocks/nuclear_bomb/destroy [ as @e[type=tnt,distance=..1,tag=!iyc.bomb] ]
#

# Lit by hand or redstone it keeps most of its 80 tick fuse, set off by another explosion it was given 10 to 30
tag @s add iyc.bomb
execute store result score #fuse iyc.data run data get entity @s fuse
execute if score #fuse iyc.data matches 60.. run data modify entity @s fuse set value 120s
execute if score #fuse iyc.data matches ..59 store result entity @s fuse short 1 run random value 15..44
data modify entity @s explosion_power set value 12.0f

