
#> iyc:shapes/wall_8/east_false/north_false/south_true/up_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_false/north_false/south_true
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/3
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/7

