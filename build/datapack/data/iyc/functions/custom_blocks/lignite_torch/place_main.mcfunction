
#> iyc:custom_blocks/lignite_torch/place_main
#
# @within	???
#

setblock ~ ~ ~ minecraft:torch
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/lignite_torch/place_secondary

