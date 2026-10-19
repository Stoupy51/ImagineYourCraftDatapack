
#> iyc:glow/refresh
#
# @executed	as @e[tag=iyc.second] & at @s
#
# @within	iyc:custom_blocks/glowstone_stairs/second
#			iyc:custom_blocks/glowstone_slab/second
#			iyc:custom_blocks/glowstone_slopes/second
#			iyc:custom_blocks/glowstone_wall/second
#			iyc:custom_blocks/glowstone_fence/second
#			iyc:custom_blocks/glowstone_fence_gate/second
#			iyc:custom_blocks/glowstone_trapdoor/second
#			iyc:custom_blocks/glowstone_pressure_plate/second
#

execute if block ~ ~1 ~ minecraft:light run return 0
execute if block ~1 ~ ~ minecraft:light run return 0
execute if block ~-1 ~ ~ minecraft:light run return 0
execute if block ~ ~ ~1 minecraft:light run return 0
execute if block ~ ~ ~-1 minecraft:light run return 0
execute if block ~ ~-1 ~ minecraft:light run return 0
execute if block ~ ~1 ~ #minecraft:air run return run setblock ~ ~1 ~ minecraft:light[level=15]
execute if block ~1 ~ ~ #minecraft:air run return run setblock ~1 ~ ~ minecraft:light[level=15]
execute if block ~-1 ~ ~ #minecraft:air run return run setblock ~-1 ~ ~ minecraft:light[level=15]
execute if block ~ ~ ~1 #minecraft:air run return run setblock ~ ~ ~1 minecraft:light[level=15]
execute if block ~ ~ ~-1 #minecraft:air run return run setblock ~ ~ ~-1 minecraft:light[level=15]
execute if block ~ ~-1 ~ #minecraft:air run return run setblock ~ ~-1 ~ minecraft:light[level=15]

