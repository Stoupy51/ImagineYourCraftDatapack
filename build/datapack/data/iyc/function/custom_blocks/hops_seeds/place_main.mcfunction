
#> iyc:custom_blocks/hops_seeds/place_main
#
# @within	???
#

tag @s add iyc.placer
setblock ~ ~ ~ minecraft:wheat
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/hops_seeds/place_secondary
tag @s remove iyc.placer

