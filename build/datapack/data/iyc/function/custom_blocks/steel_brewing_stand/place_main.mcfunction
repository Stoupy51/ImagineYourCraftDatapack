
#> iyc:custom_blocks/steel_brewing_stand/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:brewing_stand{"CustomName": {"text": "Steel Brewing Stand"}}
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/steel_brewing_stand/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_brewing_stand iyc.data 1
scoreboard players add #total_steel_brewing_stand iyc.data 1

