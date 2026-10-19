
#> iyc:shapes/ladder_13
#
# @executed	at @s
#
# @within	iyc:custom_blocks/lignite_wall_torch/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/ladder[facing=up] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=east] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=south] run return run function iyc:shapes/apply/30
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=west] run return run function iyc:shapes/apply/31
execute if block ~ ~ ~ #iyc:hosts/ladder[facing=north] run return run function iyc:shapes/apply/32

