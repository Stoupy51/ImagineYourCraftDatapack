
#> iyc:custom_blocks/iron_ladder/place_main
#
# @within	???
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air
execute if score #rotation iyc.data matches 1 run setblock ~ ~ ~ minecraft:ladder[facing=north]
execute if score #rotation iyc.data matches 2 run setblock ~ ~ ~ minecraft:ladder[facing=east]
execute if score #rotation iyc.data matches 3 run setblock ~ ~ ~ minecraft:ladder[facing=south]
execute if score #rotation iyc.data matches 4 run setblock ~ ~ ~ minecraft:ladder[facing=west]
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/iron_ladder/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_ladder iyc.data 1
scoreboard players add #total_iron_ladder iyc.data 1

