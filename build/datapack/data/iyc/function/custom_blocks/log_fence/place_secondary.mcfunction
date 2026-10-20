
#> iyc:custom_blocks/log_fence/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/log_fence/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.log_fence
tag @s add iyc.vanilla.minecraft_oak_fence

# Add a custom name
data merge entity @s {"CustomName": {"text": "Log Fence"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:log_fence"]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.fence_9
function iyc:shapes/fence_9

