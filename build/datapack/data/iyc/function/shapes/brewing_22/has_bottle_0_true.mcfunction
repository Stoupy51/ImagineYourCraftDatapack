
#> iyc:shapes/brewing_22/has_bottle_0_true
#
# @executed	at @s
#
# @within	iyc:shapes/brewing_22
#

execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_1=false] run return run function iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_false
execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_1=true] run return run function iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_true

