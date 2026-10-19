
#> iyc:custom_blocks/reversed_dark_oak_planks/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:dark_oak_planks
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/reversed_dark_oak_planks/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_dark_oak_planks iyc.data 1
scoreboard players add #total_reversed_dark_oak_planks iyc.data 1

