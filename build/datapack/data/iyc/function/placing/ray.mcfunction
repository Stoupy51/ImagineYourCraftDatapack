
#> iyc:placing/ray
#
# @executed	as @p[tag=iyc.placer] & at @s & anchored eyes & positioned ^ ^ ^ & anchored feet
#
# @within	iyc:placing/aim [ as @p[tag=iyc.placer] & at @s & anchored eyes & positioned ^ ^ ^ & anchored feet ]
#			iyc:placing/ray [ positioned ^ ^ ^0.05 ]
#

# A box test from 0.5 below a point holds when the point is in the block, from 1 below when it is in its upper half
scoreboard players add #steps iyc.data 1
execute if score #steps iyc.data matches 120.. run return 0
scoreboard players operation #was_inside iyc.data = #inside iyc.data
execute positioned ~-0.5 ~-0.5 ~-0.5 store success score #inside iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #inside iyc.data matches 1 positioned ~-0.5 ~-1 ~-0.5 store success score #upper iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #was_inside iyc.data matches 1 if score #inside iyc.data matches 0 positioned ~-0.5 ~0.5 ~-0.5 store success score #floor iyc.data if entity @e[tag=iyc.placing,dx=0,dy=0,dz=0]
execute if score #was_inside iyc.data matches 1 if score #inside iyc.data matches 0 run return 0
execute positioned ^ ^ ^0.05 run function iyc:placing/ray

