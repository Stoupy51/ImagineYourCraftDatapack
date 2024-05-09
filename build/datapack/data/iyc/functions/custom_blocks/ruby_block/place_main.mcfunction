
#> iyc:custom_blocks/ruby_block/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:diamond_block
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/ruby_block/place_secondary

