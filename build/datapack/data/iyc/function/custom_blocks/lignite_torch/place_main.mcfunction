
#> iyc:custom_blocks/lignite_torch/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon minecraft:marker run function iyc:custom_blocks/_aim/main
execute if score #floor iyc.data matches 0 run return run function iyc:custom_blocks/lignite_wall_torch/place_main

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:torch
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/lignite_torch/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_torch iyc.data 1
scoreboard players add #total_lignite_torch iyc.data 1

