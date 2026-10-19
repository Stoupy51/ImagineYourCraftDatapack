
#> iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_true/south_false/top_false
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_true/south_false
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/4
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/11

