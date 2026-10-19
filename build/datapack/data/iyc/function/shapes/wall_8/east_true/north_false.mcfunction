
#> iyc:shapes/wall_8/east_true/north_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true
#

execute if block ~ ~ ~ #iyc:hosts/wall[south=none] run return run function iyc:shapes/wall_8/east_true/north_false/south_false
execute unless block ~ ~ ~ #iyc:hosts/wall[south=none] run return run function iyc:shapes/wall_8/east_true/north_false/south_true

