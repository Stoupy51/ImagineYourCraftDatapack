
#> iyc:shapes/wall_8/east_true/north_false/south_false
#
# @executed	at @s
#
# @within	iyc:shapes/wall_8/east_true/north_false
#

execute if block ~ ~ ~ #iyc:hosts/wall[up=false] run return run function iyc:shapes/wall_8/east_true/north_false/south_false/up_false
execute if block ~ ~ ~ #iyc:hosts/wall[up=true] run return run function iyc:shapes/wall_8/east_true/north_false/south_false/up_true

