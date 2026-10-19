
#> iyc:custom_blocks/heart_effect_generator/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/heart_effect_generator/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.heart_effect_generator
tag @s add iyc.vanilla.minecraft_cobblestone

# Add a custom name
data merge entity @s {"CustomName": {"text": "Heart Effect Generator"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:heart_effect_generator"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.effect.heart
function iyc:shapes/fixed_0

# Add tag for loop every second
tag @s add iyc.second
scoreboard players add #second_entities iyc.data 1

