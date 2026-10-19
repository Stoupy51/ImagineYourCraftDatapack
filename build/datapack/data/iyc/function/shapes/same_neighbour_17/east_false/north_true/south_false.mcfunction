
#> iyc:shapes/same_neighbour_17/east_false/north_true/south_false
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_17/east_false/north_true
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/1
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/8

