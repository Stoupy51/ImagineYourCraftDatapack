
#> iyc:shapes/lamp_11
#
# @executed	at @s
#
# @within	iyc:custom_blocks/red_light/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/lamp[lit=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/lamp[lit=true] run return run function iyc:shapes/apply/1

