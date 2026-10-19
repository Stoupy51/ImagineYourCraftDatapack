
#> iyc:shapes/plate_6
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_pressure_plate/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/plate[powered=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/plate[powered=true] run return run function iyc:shapes/apply/1

