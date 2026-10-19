
#> iyc:shapes/wall_8/east_true/north_false/south_true/up_true
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true/north_false/south_true
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/6
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/12

