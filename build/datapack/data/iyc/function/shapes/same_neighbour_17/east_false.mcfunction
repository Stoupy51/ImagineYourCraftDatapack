
#> iyc:shapes/same_neighbour_17/east_false
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_17
#

execute if score #side_north iyc.data matches 0 run return run function iyc:shapes/same_neighbour_17/east_false/north_false
execute if score #side_north iyc.data matches 1 run return run function iyc:shapes/same_neighbour_17/east_false/north_true

