
#> iyc:shapes/brewing_22/has_bottle_0_false/has_bottle_1_true
#
# @executed	at @s
#
# @within	iyc:shapes/brewing_22/has_bottle_0_false
#

execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=false] run return run function iyc:shapes/apply/2
execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=true] run return run function iyc:shapes/apply/6

