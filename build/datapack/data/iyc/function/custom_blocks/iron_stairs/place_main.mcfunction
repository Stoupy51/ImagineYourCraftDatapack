
#> iyc:custom_blocks/iron_stairs/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:waxed_cut_copper_stairs
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/iron_stairs/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_waxed_cut_copper_stairs iyc.data 1
scoreboard players add #total_iron_stairs iyc.data 1

