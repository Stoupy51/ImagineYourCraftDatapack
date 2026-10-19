
#> iyc:shapes/fence_9/east_false/north_false/south_false
#
# @executed	at @s
#
# @within	iyc:shapes/fence_9/east_false/north_false
#

execute if block ~ ~ ~ #iyc:hosts/fence[west=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/fence[west=true] run return run function iyc:shapes/apply/4

