
#> iyc:shapes/furnace_21
#
# @executed	at @s
#
# @within	iyc:custom_blocks/iron_furnace/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/furnace[facing=north] run return run function iyc:shapes/furnace_21/facing_north
execute if block ~ ~ ~ #iyc:hosts/furnace[facing=south] run return run function iyc:shapes/furnace_21/facing_south
execute if block ~ ~ ~ #iyc:hosts/furnace[facing=west] run return run function iyc:shapes/furnace_21/facing_west
execute if block ~ ~ ~ #iyc:hosts/furnace[facing=east] run return run function iyc:shapes/furnace_21/facing_east

