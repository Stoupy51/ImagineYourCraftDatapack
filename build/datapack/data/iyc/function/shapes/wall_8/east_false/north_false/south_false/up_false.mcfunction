
#> iyc:shapes/wall_8/east_false/north_false/south_false/up_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_false/north_false/south_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/0
execute unless block ~ ~ ~ #iyc:hosts/wall[west=none] run return run function iyc:shapes/apply/4

