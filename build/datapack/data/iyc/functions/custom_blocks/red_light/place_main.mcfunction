
#> iyc:custom_blocks/red_light/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:red_concrete
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/red_light/place_secondary

