
#> iyc:custom_blocks/glowstone_fence_gate/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_fence_gate/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.glowstone_fence_gate
tag @s add iyc.vanilla.minecraft_oak_fence_gate

# Add a custom name
data merge entity @s {"CustomName": {"text": "Glowstone Fence Gate"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:glowstone_fence_gate"]
function iyc:custom_blocks/compute_brightness

# Apply rotation
execute if score #rotation iyc.data matches 1 run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 2 run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 3 run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 4 run data modify entity @s Rotation[0] set value 90.0f

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.gate_10
function iyc:shapes/gate_10

