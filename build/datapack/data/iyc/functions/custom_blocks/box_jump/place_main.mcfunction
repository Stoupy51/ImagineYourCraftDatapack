
#> iyc:custom_blocks/box_jump/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:oak_planks
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/box_jump/place_secondary

