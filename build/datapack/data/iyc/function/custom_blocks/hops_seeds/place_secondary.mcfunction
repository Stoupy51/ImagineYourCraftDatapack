
#> iyc:custom_blocks/hops_seeds/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/hops_seeds/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.hops_seeds
tag @s add iyc.vanilla.minecraft_wheat
tag @s add iyc.growing_seed

# Add a custom name
data merge entity @s {"CustomName": {"text": "Hops Seeds"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:hops_seeds"]
function iyc:custom_blocks/compute_brightness

# Update seed model
scoreboard players add @s iyc.growth_time 0
function iyc:custom_blocks/hops_seeds/update_seed_model

# Add tag for loop every minute
tag @s add iyc.minute
scoreboard players add #minute_entities iyc.data 1

