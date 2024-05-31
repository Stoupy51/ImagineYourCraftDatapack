
#> iyc:custom_blocks/lignite_block/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ minecraft:coal_block
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/lignite_block/place_secondary
tag @s remove iyc.placer

