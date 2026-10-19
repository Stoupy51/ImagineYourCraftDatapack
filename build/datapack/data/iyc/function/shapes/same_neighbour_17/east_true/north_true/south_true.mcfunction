
#> iyc:shapes/same_neighbour_17/east_true/north_true/south_true
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_17/east_true/north_true
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/11
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/15

