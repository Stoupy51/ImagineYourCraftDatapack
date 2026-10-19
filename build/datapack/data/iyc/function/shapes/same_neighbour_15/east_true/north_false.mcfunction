
#> iyc:shapes/same_neighbour_15/east_true/north_false
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_15/east_true
#

execute if score #side_south iyc.data matches 0 run return run function iyc:shapes/same_neighbour_15/east_true/north_false/south_false
execute if score #side_south iyc.data matches 1 run return run function iyc:shapes/same_neighbour_15/east_true/north_false/south_true

