
#> iyc:shapes/slope_2/facing_west
#
# @executed	at @s
#
# @within	iyc:shapes/slope_2
#

execute if score #upper iyc.data matches 0 run return run function iyc:shapes/apply/1
execute if score #upper iyc.data matches 1 run return run function iyc:shapes/apply/5

