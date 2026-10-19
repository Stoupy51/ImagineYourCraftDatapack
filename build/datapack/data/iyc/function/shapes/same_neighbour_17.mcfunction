
#> iyc:shapes/same_neighbour_17
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_bench/place_secondary
#			iyc:custom_blocks/birch_bench/place_secondary
#			iyc:custom_blocks/cobblestone_bench/place_secondary
#			iyc:custom_blocks/stone_bench/place_secondary
#			iyc:shapes/follow
#

execute store success score #side_east iyc.data positioned ~0.5 ~-0.5 ~-0.5 if entity @e[type=item_display,tag=iyc.connect.bench,dx=0,dy=0,dz=0]
execute store success score #side_north iyc.data positioned ~-0.5 ~-0.5 ~-1.5 if entity @e[type=item_display,tag=iyc.connect.bench,dx=0,dy=0,dz=0]
execute store success score #side_south iyc.data positioned ~-0.5 ~-0.5 ~0.5 if entity @e[type=item_display,tag=iyc.connect.bench,dx=0,dy=0,dz=0]
execute store success score #side_west iyc.data positioned ~-1.5 ~-0.5 ~-0.5 if entity @e[type=item_display,tag=iyc.connect.bench,dx=0,dy=0,dz=0]
execute if score #side_east iyc.data matches 0 run return run function iyc:shapes/same_neighbour_17/east_false
execute if score #side_east iyc.data matches 1 run return run function iyc:shapes/same_neighbour_17/east_true

