
#> iyc:custom_blocks/deepslate_adamantium_ore/place_main
#
# @within	iyc:custom_blocks/place
#			iyc:interaction/light
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~-0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~-0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~-0.4 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.0 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.0 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.0 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~-0.4 ~0.4 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~-0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~-0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~-0.4 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.0 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.0 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.0 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.0 ~0.4 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~-0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~-0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~-0.4 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.0 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.0 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.0 ~0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.4 ~-0.4 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.4 ~0.0 ]
#			iyc:calls/smart_ore_generation/veins/deepslate_adamantium_ore [ at @s & positioned ~0.4 ~0.4 ~0.4 ]
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:polished_deepslate
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/deepslate_adamantium_ore/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_polished_deepslate iyc.data 1
scoreboard players add #total_deepslate_adamantium_ore iyc.data 1

