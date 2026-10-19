
#> iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_true/south_true/top_false
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_true/south_true
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/36
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/40

