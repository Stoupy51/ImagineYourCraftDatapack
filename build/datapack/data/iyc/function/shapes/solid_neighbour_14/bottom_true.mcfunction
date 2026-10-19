
#> iyc:shapes/solid_neighbour_14/bottom_true
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14
#

execute if score #side_east iyc.data matches 0 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_false
execute if score #side_east iyc.data matches 1 run return run function iyc:shapes/solid_neighbour_14/bottom_true/east_true

