
#> iyc:custom_blocks/gray_lamp/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:structure_void
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/gray_lamp/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_structure_void iyc.data 1
scoreboard players add #total_gray_lamp iyc.data 1

