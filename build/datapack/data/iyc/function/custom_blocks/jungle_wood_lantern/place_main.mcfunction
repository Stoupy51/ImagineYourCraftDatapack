
#> iyc:custom_blocks/jungle_wood_lantern/place_main
#
# @within	iyc:custom_blocks/place
#

setblock ~ ~ ~ minecraft:ochre_froglight
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/jungle_wood_lantern/place_secondary

