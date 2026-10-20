
#> iyc:custom_blocks/step_block/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/step_block/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.step_block
tag @s add iyc.vanilla.minecraft_smooth_stone

# Add a custom name
data merge entity @s {"CustomName": {"text": "Step Block"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:step_block"]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
function iyc:shapes/fixed_0

