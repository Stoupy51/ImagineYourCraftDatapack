
# Check for bolts
execute as @e[type=arrow,tag=!imagineyourcraft.bolt_checked] run function imagineyourcraft:entity/bolt_check

# Check for rocks
execute if score #rock_markers imagineyourcraft.data matches 1.. as @e[tag=imagineyourcraft.rock_marker,predicate=!imagineyourcraft:has_vehicle] at @s positioned ~ ~-0.5 ~ run function imagineyourcraft:entity/rock_check/marker_final
execute as @e[type=snowball,tag=!imagineyourcraft.rock_checked] run function imagineyourcraft:entity/rock_check/main

