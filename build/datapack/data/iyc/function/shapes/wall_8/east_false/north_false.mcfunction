
#> iyc:shapes/wall_8/east_false/north_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[south=none] run return run function iyc:shapes/wall_8/east_false/north_false/south_false
execute unless block ~ ~ ~ #iyc:hosts/wall[south=none] run return run function iyc:shapes/wall_8/east_false/north_false/south_true

