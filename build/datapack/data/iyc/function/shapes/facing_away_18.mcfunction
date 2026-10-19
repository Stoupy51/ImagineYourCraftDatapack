
#> iyc:shapes/facing_away_18
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_chair/place_secondary
#			iyc:custom_blocks/birch_chair/place_secondary
#			iyc:custom_blocks/cobblestone_chair/place_secondary
#			iyc:custom_blocks/stone_chair/place_secondary
#

execute if score #rotation iyc.data matches 1 run return run function iyc:shapes/apply/0
execute if score #rotation iyc.data matches 3 run return run function iyc:shapes/apply/28
execute if score #rotation iyc.data matches 4 run return run function iyc:shapes/apply/29
execute if score #rotation iyc.data matches 2 run return run function iyc:shapes/apply/27

