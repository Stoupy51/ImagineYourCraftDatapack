
#> iyc:custom_blocks/red_light/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ minecraft:red_concrete
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/red_light/place_secondary
tag @s remove iyc.placer

