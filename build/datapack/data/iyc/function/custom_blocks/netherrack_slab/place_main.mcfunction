
#> iyc:custom_blocks/netherrack_slab/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon marker run function iyc:custom_blocks/_aim/main
setblock ~ ~ ~ air strict
execute if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:nether_brick_slab[type=bottom]
execute if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:nether_brick_slab[type=top]
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/netherrack_slab/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_nether_brick_slab iyc.data 1
scoreboard players add #total_netherrack_slab iyc.data 1

