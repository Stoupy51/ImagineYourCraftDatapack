
#> iyc:custom_blocks/steel_ore/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:polished_deepslate
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/steel_ore/place_secondary

