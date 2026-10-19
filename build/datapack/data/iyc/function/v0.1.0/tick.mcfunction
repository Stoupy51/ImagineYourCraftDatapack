
#> iyc:v0.1.0/tick
#
# @within	iyc:v0.1.0/load/tick_verification
#

# Timers
scoreboard players add #tick_2 iyc.data 1
scoreboard players add #second iyc.data 1
scoreboard players add #second_5 iyc.data 1
scoreboard players add #minute iyc.data 1
execute if score #tick_2 iyc.data matches 3.. run function iyc:v0.1.0/tick_2
execute if score #second iyc.data matches 20.. run function iyc:v0.1.0/second
execute if score #second_5 iyc.data matches 90.. run function iyc:v0.1.0/second_5
execute if score #minute iyc.data matches 1200.. run function iyc:v0.1.0/minute

execute as @e[type=item_display,tag=iyc.seat,predicate=!iyc:has_passenger] run kill @s

# Check for bolts
execute as @e[type=arrow,tag=!iyc.bolt_checked] run function iyc:entity/bolt_check

# Check for rocks
execute if score #rock_markers iyc.data matches 1.. as @e[tag=iyc.rock_marker,predicate=!iyc:has_vehicle] at @s positioned ~ ~-0.5 ~ run function iyc:entity/rock_check/marker_final
execute as @e[type=snowball,tag=!iyc.rock_checked] run function iyc:entity/rock_check/main

# Clouds and flowers touched by living entities, players cancelling their fall through slow falling since their fall distance is read only
execute as @a[gamemode=!spectator] at @s if block ~ ~ ~ minecraft:structure_void if entity @e[type=item_display,tag=iyc.cloud,distance=..0.9] run effect give @s minecraft:slow_falling 1 0 true
execute as @a[gamemode=!spectator,gamemode=!creative] at @s if block ~ ~ ~ minecraft:tripwire run function iyc:flowers/touch
execute as @e[type=!player,type=!#iyc:not_living] at @s if block ~ ~ ~ #iyc:touched_hosts run function iyc:mob_touch

# Stairs, slopes and slabs standing on a barrier climbed without jumping, as their own collision allowed
execute as @a[tag=!iyc.stepping] at @s if entity @e[type=item_display,tag=iyc.step,distance=..1.8] run function iyc:step/enter
execute as @a[tag=iyc.stepping] at @s unless entity @e[type=item_display,tag=iyc.step,distance=..1.8] run function iyc:step/leave

# Jump box launches
execute as @a[tag=iyc.launched] run function iyc:jump_box/flight

# Custom blocks tick functions
execute if score #tick_entities iyc.data matches 1.. as @e[tag=iyc.tick] at @s run function iyc:custom_blocks/tick

