
#> iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false
#

execute if score #side_top iyc.data matches 1 run return run function iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_true
execute if score #side_top iyc.data matches 0 run return run function iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_false

