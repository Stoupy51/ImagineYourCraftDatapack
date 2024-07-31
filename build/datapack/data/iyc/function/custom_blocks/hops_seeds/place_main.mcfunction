
#> iyc:custom_blocks/hops_seeds/place_main
#
# @within	???
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:wheat
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/hops_seeds/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_wheat iyc.data 1
scoreboard players add #total_hops_seeds iyc.data 1

