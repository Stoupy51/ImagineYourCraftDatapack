
#> iyc:shapes/same_neighbour_17/east_false/north_true
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_17/east_false
#

execute if score #side_south iyc.data matches 0 run return run function iyc:shapes/same_neighbour_17/east_false/north_true/south_false
execute if score #side_south iyc.data matches 1 run return run function iyc:shapes/same_neighbour_17/east_false/north_true/south_true

