
#> iyc:custom_blocks/iron_fence_gate/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:oak_fence_gate
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/iron_fence_gate/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_oak_fence_gate iyc.data 1
scoreboard players add #total_iron_fence_gate iyc.data 1

