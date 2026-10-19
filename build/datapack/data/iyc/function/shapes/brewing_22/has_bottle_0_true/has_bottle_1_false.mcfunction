
#> iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_false
#
# @executed	at @s
#
# @within	iyc:shapes/brewing_22/has_bottle_0_true
#

execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=false] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/brewing[has_bottle_2=true] run return run function iyc:shapes/apply/5

