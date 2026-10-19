
#> iyc:shapes/fence_9/east_false/north_false
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_false
#

execute if block ~ ~ ~ #iyc:hosts/fence[south=false] run return run function iyc:shapes/fence_9/east_false/north_false/south_false
execute if block ~ ~ ~ #iyc:hosts/fence[south=true] run return run function iyc:shapes/fence_9/east_false/north_false/south_true

