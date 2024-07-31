
#> iyc:custom_blocks/clear_glass/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:structure_void
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/clear_glass/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_structure_void iyc.data 1
scoreboard players add #total_clear_glass iyc.data 1

