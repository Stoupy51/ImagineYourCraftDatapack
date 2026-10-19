
#> iyc:custom_blocks/glowstone_pressure_plate/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:stone_pressure_plate
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/glowstone_pressure_plate/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_stone_pressure_plate iyc.data 1
scoreboard players add #total_glowstone_pressure_plate iyc.data 1

