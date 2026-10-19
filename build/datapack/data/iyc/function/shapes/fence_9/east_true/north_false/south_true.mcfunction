
#> iyc:shapes/fence_9/east_true/north_false/south_true
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_true/north_false
#

execute if block ~ ~ ~ #iyc:hosts/fence[west=false] run return run function iyc:shapes/apply/6
execute if block ~ ~ ~ #iyc:hosts/fence[west=true] run return run function iyc:shapes/apply/12

