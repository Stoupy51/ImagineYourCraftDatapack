
#> iyc:shapes/fence_9/east_true
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9
#

execute if block ~ ~ ~ #iyc:hosts/fence[north=false] run return run function iyc:shapes/fence_9/east_true/north_false
execute if block ~ ~ ~ #iyc:hosts/fence[north=true] run return run function iyc:shapes/fence_9/east_true/north_true

