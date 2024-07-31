
#> iyc:custom_blocks/lignite_torch/place_main
#
# @within	???
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:torch
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/lignite_torch/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_torch iyc.data 1
scoreboard players add #total_lignite_torch iyc.data 1

