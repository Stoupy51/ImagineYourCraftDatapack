
#> iyc:custom_blocks/iron_furnace/tick
#
# @executed	as @e[tag=iyc.tick] & at @s
#
# @within	iyc:custom_blocks/tick
#

# Cook 2.0 times faster, never reaching the end itself so vanilla still finishes the item
execute unless block ~ ~ ~ minecraft:furnace[lit=true] run return 0
execute store result score #spent iyc.data run data get block ~ ~ ~ cooking_time_spent
execute if score #spent iyc.data matches 0 run return 0
execute store result score #total iyc.data run data get block ~ ~ ~ cooking_total_time
scoreboard players add #spent iyc.data 1

execute if score #spent iyc.data >= #total iyc.data run scoreboard players operation #spent iyc.data = #total iyc.data
execute if score #spent iyc.data = #total iyc.data run scoreboard players remove #spent iyc.data 1
execute store result block ~ ~ ~ cooking_time_spent int 1 run scoreboard players get #spent iyc.data

