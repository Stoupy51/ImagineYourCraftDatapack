
#> iyc:shapes/brewing_22
#
# @executed	at @s
#
# @within	iyc:custom_blocks/steel_brewing_stand/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_0=false] run return run function iyc:shapes/brewing_22/has_bottle_0_false
execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_0=true] run return run function iyc:shapes/brewing_22/has_bottle_0_true

