
#> iyc:shapes/wall_8/east_true/north_true/south_false/up_true
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true/north_true/south_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/5
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/14

