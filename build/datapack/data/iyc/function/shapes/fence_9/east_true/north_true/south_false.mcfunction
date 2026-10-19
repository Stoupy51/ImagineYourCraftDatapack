
#> iyc:shapes/fence_9/east_true/north_true/south_false
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_true/north_true
#

execute if block ~ ~ ~ #iyc:hosts/fence[west=false] run return run function iyc:shapes/apply/5
execute if block ~ ~ ~ #iyc:hosts/fence[west=true] run return run function iyc:shapes/apply/14

