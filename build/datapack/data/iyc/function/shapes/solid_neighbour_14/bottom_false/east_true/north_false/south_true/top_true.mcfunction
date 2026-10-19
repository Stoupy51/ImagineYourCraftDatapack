
#> iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_true/top_true
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_true
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/9
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/15

