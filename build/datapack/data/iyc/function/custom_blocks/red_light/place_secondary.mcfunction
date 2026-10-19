
#> iyc:custom_blocks/red_light/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/red_light/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.red_light
tag @s add iyc.vanilla.minecraft_redstone_lamp

# Add a custom name
data merge entity @s {"CustomName": {"text": "Red Light"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:red_light"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.lamp_11
function iyc:shapes/lamp_11

