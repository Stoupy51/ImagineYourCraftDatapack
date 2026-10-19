
#> iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_true
#
# @executed	at @s
#
# @within	iyc:shapes/brewing_22/has_bottle_0_true
#

execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=false] run return run function iyc:shapes/apply/4
execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=true] run return run function iyc:shapes/apply/7

