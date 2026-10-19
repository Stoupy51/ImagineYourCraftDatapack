
#> iyc:shapes/facing_player_19
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_shelf/place_secondary
#

execute if score #rotation iyc.data matches 3 run return run function iyc:shapes/apply/0
execute if score #rotation iyc.data matches 1 run return run function iyc:shapes/apply/28
execute if score #rotation iyc.data matches 2 run return run function iyc:shapes/apply/29
execute if score #rotation iyc.data matches 4 run return run function iyc:shapes/apply/27

