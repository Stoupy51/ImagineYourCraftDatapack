
#> iyc:custom_blocks/slate_stairs/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon marker run function iyc:custom_blocks/_aim/main
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air strict
execute if score #rotation iyc.data matches 1 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:stone_stairs[half=bottom,facing=south]
execute if score #rotation iyc.data matches 1 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:stone_stairs[half=top,facing=south]
execute if score #rotation iyc.data matches 2 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:stone_stairs[half=bottom,facing=west]
execute if score #rotation iyc.data matches 2 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:stone_stairs[half=top,facing=west]
execute if score #rotation iyc.data matches 3 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:stone_stairs[half=bottom,facing=north]
execute if score #rotation iyc.data matches 3 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:stone_stairs[half=top,facing=north]
execute if score #rotation iyc.data matches 4 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:stone_stairs[half=bottom,facing=east]
execute if score #rotation iyc.data matches 4 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:stone_stairs[half=top,facing=east]
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/slate_stairs/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_stone_stairs iyc.data 1
scoreboard players add #total_slate_stairs iyc.data 1

