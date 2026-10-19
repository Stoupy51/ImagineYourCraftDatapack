
#> iyc:flowers/touch
#
# @executed	as @a[gamemode=!spectator] & at @s
#
# @within	iyc:v0.1.0/tick [ as @a[gamemode=!spectator] & at @s ]
#			iyc:mob_touch
#

# Poison and slowness last 100 ticks, 150 in normal and 300 in hard (gc_1, hm_1)
execute store result score #difficulty iyc.data run difficulty
execute if entity @e[type=item_display,tag=iyc.blue_flower,distance=..0.9] run function iyc:flowers/effect {effect:"poison"}
execute if entity @e[type=item_display,tag=iyc.white_flower,distance=..0.9] run function iyc:flowers/effect {effect:"slowness"}
execute if entity @e[type=item_display,tag=iyc.black_flower,distance=..0.9] run damage @s 1 minecraft:cactus

