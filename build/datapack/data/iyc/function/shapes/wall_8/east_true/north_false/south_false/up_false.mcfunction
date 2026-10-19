
#> iyc:shapes/wall_8/east_true/north_false/south_false/up_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true/north_false/south_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/2
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/10

