
#> iyc:custom_blocks/cherry_cake/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ minecraft:cake
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/cherry_cake/place_secondary
tag @s remove iyc.placer

