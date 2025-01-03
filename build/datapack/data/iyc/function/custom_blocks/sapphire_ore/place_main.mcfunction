
#> iyc:custom_blocks/sapphire_ore/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:calls/smart_ore_generation/veins/sapphire_ore
#

tag @s add iyc.placer
setblock ~ ~ ~ air
setblock ~ ~ ~ minecraft:polished_deepslate
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/sapphire_ore/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_polished_deepslate iyc.data 1
scoreboard players add #total_sapphire_ore iyc.data 1

