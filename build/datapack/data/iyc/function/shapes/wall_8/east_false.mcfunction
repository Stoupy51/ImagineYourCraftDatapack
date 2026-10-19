
#> iyc:shapes/wall_8/east_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8
#

execute if block ~ ~ ~ #iyc:hosts/wall[north=none] run return run function iyc:shapes/wall_8/east_false/north_false
execute unless block ~ ~ ~ #iyc:hosts/wall[north=none] run return run function iyc:shapes/wall_8/east_false/north_true

