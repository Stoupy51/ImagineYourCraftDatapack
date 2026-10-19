
#> iyc:shapes/gate_10
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_fence_gate/place_secondary
#			iyc:custom_blocks/log_fence_gate/place_secondary
#			iyc:custom_blocks/stone_fence_gate/place_secondary
#			iyc:custom_blocks/iron_fence_gate/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/gate[facing=south] run return run function iyc:shapes/gate_10/facing_south
execute if block ~ ~ ~ #iyc:hosts/gate[facing=west] run return run function iyc:shapes/gate_10/facing_west
execute if block ~ ~ ~ #iyc:hosts/gate[facing=north] run return run function iyc:shapes/gate_10/facing_north
execute if block ~ ~ ~ #iyc:hosts/gate[facing=east] run return run function iyc:shapes/gate_10/facing_east

