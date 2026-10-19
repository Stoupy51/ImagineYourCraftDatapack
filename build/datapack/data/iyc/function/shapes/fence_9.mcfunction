
#> iyc:shapes/fence_9
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_fence/place_secondary
#			iyc:custom_blocks/log_fence/place_secondary
#			iyc:custom_blocks/stone_fence/place_secondary
#			iyc:custom_blocks/white_iron_fence/place_secondary
#			iyc:custom_blocks/orange_iron_fence/place_secondary
#			iyc:custom_blocks/magenta_iron_fence/place_secondary
#			iyc:custom_blocks/light_blue_iron_fence/place_secondary
#			iyc:custom_blocks/yellow_iron_fence/place_secondary
#			iyc:custom_blocks/lime_iron_fence/place_secondary
#			iyc:custom_blocks/pink_iron_fence/place_secondary
#			iyc:custom_blocks/gray_iron_fence/place_secondary
#			iyc:custom_blocks/light_gray_iron_fence/place_secondary
#			iyc:custom_blocks/cyan_iron_fence/place_secondary
#			iyc:custom_blocks/purple_iron_fence/place_secondary
#			iyc:custom_blocks/blue_iron_fence/place_secondary
#			iyc:custom_blocks/brown_iron_fence/place_secondary
#			iyc:custom_blocks/green_iron_fence/place_secondary
#			iyc:custom_blocks/red_iron_fence/place_secondary
#			iyc:custom_blocks/black_iron_fence/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/fence[east=false] run return run function iyc:shapes/fence_9/east_false
execute if block ~ ~ ~ #iyc:hosts/fence[east=true] run return run function iyc:shapes/fence_9/east_true

