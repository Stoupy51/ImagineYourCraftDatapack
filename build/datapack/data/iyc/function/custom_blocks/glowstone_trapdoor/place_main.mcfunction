
#> iyc:custom_blocks/glowstone_trapdoor/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:oak_trapdoor
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/glowstone_trapdoor/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_oak_trapdoor iyc.data 1
scoreboard players add #total_glowstone_trapdoor iyc.data 1

