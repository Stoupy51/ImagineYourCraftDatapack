
#> iyc:custom_blocks/white_flower/place_main
#
# @within	???
#

setblock ~ ~ ~ minecraft:structure_void
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/white_flower/place_secondary
