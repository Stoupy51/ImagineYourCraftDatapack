
#> iyc:shapes/fence_9/east_false/north_true
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_false
#

execute if block ~ ~ ~ #iyc:hosts/fence[south=false] run return run function iyc:shapes/fence_9/east_false/north_true/south_false
execute if block ~ ~ ~ #iyc:hosts/fence[south=true] run return run function iyc:shapes/fence_9/east_false/north_true/south_true

