
#> iyc:custom_blocks/sapphire_block/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:diamond_block
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/sapphire_block/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_diamond_block iyc.data 1
scoreboard players add #total_sapphire_block iyc.data 1

