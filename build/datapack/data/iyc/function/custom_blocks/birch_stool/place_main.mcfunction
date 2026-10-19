
#> iyc:custom_blocks/birch_stool/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:barrier
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/birch_stool/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_barrier iyc.data 1
scoreboard players add #total_birch_stool iyc.data 1

