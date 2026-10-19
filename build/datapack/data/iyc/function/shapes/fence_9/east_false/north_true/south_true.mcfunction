
#> iyc:shapes/fence_9/east_false/north_true/south_true
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_false/north_true
#

execute if block ~ ~ ~ #iyc:hosts/fence[west=false] run return run function iyc:shapes/apply/9
execute if block ~ ~ ~ #iyc:hosts/fence[west=true] run return run function iyc:shapes/apply/13

