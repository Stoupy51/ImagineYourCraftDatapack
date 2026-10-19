
#> iyc:shapes/same_neighbour_17/east_true
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_17
#

execute if score #side_north iyc.data matches 0 run return run function iyc:shapes/same_neighbour_17/east_true/north_false
execute if score #side_north iyc.data matches 1 run return run function iyc:shapes/same_neighbour_17/east_true/north_true

