
#> iyc:glow/clear
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_stairs/destroy
#			iyc:custom_blocks/glowstone_slopes/destroy
#			iyc:custom_blocks/glowstone_slab/destroy
#			iyc:custom_blocks/glowstone_trapdoor/destroy
#			iyc:custom_blocks/glowstone_pressure_plate/destroy
#			iyc:custom_blocks/glowstone_wall/destroy
#			iyc:custom_blocks/glowstone_fence/destroy
#			iyc:custom_blocks/glowstone_fence_gate/destroy
#

execute positioned ~ ~1 ~ if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air
execute positioned ~1 ~ ~ if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air
execute positioned ~-1 ~ ~ if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air
execute positioned ~ ~ ~1 if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air
execute positioned ~ ~ ~-1 if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air
execute positioned ~ ~-1 ~ if block ~ ~ ~ minecraft:light unless entity @e[type=item_display,tag=iyc.custom_block,distance=..0.5] run setblock ~ ~ ~ air

