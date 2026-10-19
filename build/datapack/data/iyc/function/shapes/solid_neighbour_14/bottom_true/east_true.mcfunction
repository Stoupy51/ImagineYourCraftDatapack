
#> iyc:shapes/solid_neighbour_14/bottom_true/east_true
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_true
#

execute if score #side_north iyc.data matches 0 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_true/north_false
execute if score #side_north iyc.data matches 1 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_true/north_true

