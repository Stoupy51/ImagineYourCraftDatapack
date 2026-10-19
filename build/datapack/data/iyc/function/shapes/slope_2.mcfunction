
#> iyc:shapes/slope_2
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glass_stairs/place_secondary
#			iyc:custom_blocks/stone_slopes/place_secondary
#			iyc:custom_blocks/slate_slopes/place_secondary
#			iyc:custom_blocks/sandstone_slopes/place_secondary
#			iyc:custom_blocks/glowstone_slopes/place_secondary
#			iyc:custom_blocks/oak_planks_slopes/place_secondary
#			iyc:custom_blocks/spruce_planks_slopes/place_secondary
#			iyc:custom_blocks/birch_planks_slopes/place_secondary
#			iyc:custom_blocks/jungle_planks_slopes/place_secondary
#			iyc:custom_blocks/oak_log_slopes/place_secondary
#			iyc:custom_blocks/spruce_log_slopes/place_secondary
#			iyc:custom_blocks/birch_log_slopes/place_secondary
#			iyc:custom_blocks/jungle_log_slopes/place_secondary
#			iyc:custom_blocks/glass_slopes/place_secondary
#

execute if score #rotation iyc.data matches 4 run return run function iyc:shapes/slope_2/facing_east
execute if score #rotation iyc.data matches 2 run return run function iyc:shapes/slope_2/facing_west
execute if score #rotation iyc.data matches 1 run return run function iyc:shapes/slope_2/facing_south
execute if score #rotation iyc.data matches 3 run return run function iyc:shapes/slope_2/facing_north

