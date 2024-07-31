
#> iyc:custom_blocks/jungle_wood_lantern/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:ochre_froglight
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/jungle_wood_lantern/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_ochre_froglight iyc.data 1
scoreboard players add #total_jungle_wood_lantern iyc.data 1

