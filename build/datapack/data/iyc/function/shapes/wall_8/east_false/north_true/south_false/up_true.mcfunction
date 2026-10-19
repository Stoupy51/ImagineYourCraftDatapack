
#> iyc:shapes/wall_8/east_false/north_true/south_false/up_true
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_false/north_true/south_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/1
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/8

