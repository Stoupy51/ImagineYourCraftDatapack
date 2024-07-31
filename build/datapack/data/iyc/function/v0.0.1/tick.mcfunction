
#> iyc:v0.0.1/tick
#
# @within	iyc:v0.0.1/load/tick_verification
#

# Timers
scoreboard players add #tick_2 iyc.data 1
scoreboard players add #second iyc.data 1
scoreboard players add #second_5 iyc.data 1
execute if score #tick_2 iyc.data matches 3.. run function iyc:v0.0.1/tick_2
execute if score #second iyc.data matches 20.. run function iyc:v0.0.1/second
execute if score #second_5 iyc.data matches 90.. run function iyc:v0.0.1/second_5

