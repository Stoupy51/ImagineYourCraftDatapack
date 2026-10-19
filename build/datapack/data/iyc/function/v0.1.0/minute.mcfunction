
#> iyc:v0.1.0/minute
#
# @within	iyc:v0.1.0/tick
#

# Reset timer
scoreboard players set #minute iyc.data 1

# Custom blocks minute functions
execute if score #minute_entities iyc.data matches 1.. as @e[tag=iyc.minute] at @s run function iyc:custom_blocks/minute

