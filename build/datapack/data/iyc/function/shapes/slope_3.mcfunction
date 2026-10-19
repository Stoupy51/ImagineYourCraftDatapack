
#> iyc:shapes/slope_3
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glass_slab/place_secondary
#

execute if score #upper iyc.data matches 0 run return run function iyc:shapes/apply/0
execute if score #upper iyc.data matches 1 run return run function iyc:shapes/apply/1

