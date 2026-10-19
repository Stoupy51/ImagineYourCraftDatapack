
#> iyc:shapes/wall_8
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_log_wall/place_secondary
#			iyc:custom_blocks/stone_wall/place_secondary
#			iyc:custom_blocks/oak_plank_wall/place_secondary
#			iyc:custom_blocks/glowstone_wall/place_secondary
#			iyc:custom_blocks/slate_wall/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/wall[east=none] run return run function iyc:shapes/wall_8/east_false
execute unless block ~ ~ ~ #iyc:hosts/wall[east=none] run return run function iyc:shapes/wall_8/east_true

