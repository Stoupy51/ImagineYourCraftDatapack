
#> iyc:shapes/ladder_7
#
# @executed	at @s
#
# @within	iyc:custom_blocks/iron_ladder/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/ladder[facing=north] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=east] run return run function iyc:shapes/apply/27
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=south] run return run function iyc:shapes/apply/28
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=west] run return run function iyc:shapes/apply/29

