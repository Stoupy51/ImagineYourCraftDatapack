
#> iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_false
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_true/east_false
#

execute if score #side_south iyc.data matches 0 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_false/south_false
execute if score #side_south iyc.data matches 1 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_false/south_true

