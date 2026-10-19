
#> iyc:shapes/same_neighbour_16/east_false/north_false/south_true
#
# @executed	at @s
#
# @within	iyc:shapes/same_neighbour_16/east_false/north_false
#

execute if score #side_west iyc.data matches 0 run return run function iyc:shapes/apply/3
execute if score #side_west iyc.data matches 1 run return run function iyc:shapes/apply/7

