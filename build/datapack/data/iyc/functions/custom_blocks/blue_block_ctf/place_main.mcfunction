
#> iyc:custom_blocks/blue_block_ctf/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:glass
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/blue_block_ctf/place_secondary

