
#> iyc:tick
#
# @within	???
#

# Check for bolts
execute as @e[type=arrow,tag=!iyc.bolt_checked] run function iyc:entity/bolt_check

# Check for rocks
execute if score #rock_markers iyc.data matches 1.. as @e[tag=iyc.rock_marker,predicate=!iyc:has_vehicle] at @s positioned ~ ~-0.5 ~ run function iyc:entity/rock_check/marker_final
execute as @e[type=snowball,tag=!iyc.rock_checked] run function iyc:entity/rock_check/main

