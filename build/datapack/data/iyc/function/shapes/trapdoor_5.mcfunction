
#> iyc:shapes/trapdoor_5
#
# @executed	at @s
#
# @within	iyc:custom_blocks/stone_trapdoor/place_secondary
#			iyc:custom_blocks/glowstone_trapdoor/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/trapdoor[facing=north] run return run function iyc:shapes/trapdoor_5/facing_north
execute if block ~ ~ ~ #iyc:hosts/trapdoor[facing=south] run return run function iyc:shapes/trapdoor_5/facing_south
execute if block ~ ~ ~ #iyc:hosts/trapdoor[facing=east] run return run function iyc:shapes/trapdoor_5/facing_east
execute if block ~ ~ ~ #iyc:hosts/trapdoor[facing=west] run return run function iyc:shapes/trapdoor_5/facing_west

