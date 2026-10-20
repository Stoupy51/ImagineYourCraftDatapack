
#> iyc:custom_blocks/steel_brewing_stand/tick
#
# @executed	as @e[tag=iyc.tick] & at @s
#
# @within	iyc:custom_blocks/tick
#

# Brew 1.6 times faster
execute store result score #brew iyc.data run data get block ~ ~ ~ BrewTime
execute if score #brew iyc.data matches ..2 run return 0

execute if score #brew iyc.data matches 3.. if predicate {"type": "minecraft:random_chance","chance": 0.6} run scoreboard players remove #brew iyc.data 1
execute store result block ~ ~ ~ BrewTime short 1 run scoreboard players get #brew iyc.data

