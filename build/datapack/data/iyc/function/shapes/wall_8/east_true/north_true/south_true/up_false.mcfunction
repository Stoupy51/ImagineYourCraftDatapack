
#> iyc:shapes/wall_8/east_true/north_true/south_true/up_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true/north_true/south_true
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/11
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/15

