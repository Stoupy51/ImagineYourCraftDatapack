
#> iyc:custom_blocks/box_speed/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/box_speed/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.box_speed
tag @s add iyc.vanilla.minecraft_oak_planks

# Add a custom name
data merge entity @s {"CustomName": {"text": "Box Speed"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:box_speed"]
function iyc:custom_blocks/compute_brightness

# Add tag for loop every tick
tag @s add iyc.tick
scoreboard players add #tick_entities iyc.data 1

