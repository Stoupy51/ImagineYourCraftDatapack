
#> iyc:shapes/stairs_1
#
# @executed	at @s
#
# @within	iyc:custom_blocks/log_stairs/place_secondary
#			iyc:custom_blocks/glowstone_stairs/place_secondary
#			iyc:custom_blocks/iron_stairs/place_secondary
#			iyc:custom_blocks/obsidian_stairs/place_secondary
#			iyc:custom_blocks/step_stairs/place_secondary
#			iyc:custom_blocks/slate_stairs/place_secondary
#			iyc:custom_blocks/oak_reversed_planks_stairs/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/stairs[facing=east] run return run function iyc:shapes/stairs_1/facing_east
execute if block ~ ~ ~ #iyc:hosts/stairs[facing=west] run return run function iyc:shapes/stairs_1/facing_west
execute if block ~ ~ ~ #iyc:hosts/stairs[facing=south] run return run function iyc:shapes/stairs_1/facing_south
execute if block ~ ~ ~ #iyc:hosts/stairs[facing=north] run return run function iyc:shapes/stairs_1/facing_north

