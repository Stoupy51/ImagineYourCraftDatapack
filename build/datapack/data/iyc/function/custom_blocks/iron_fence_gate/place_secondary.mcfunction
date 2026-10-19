
#> iyc:custom_blocks/iron_fence_gate/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/iron_fence_gate/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.iron_fence_gate
tag @s add iyc.vanilla.minecraft_oak_fence_gate

# Add a custom name
data merge entity @s {"CustomName": {"text": "Iron Fence Gate"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:iron_fence_gate"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
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
function iyc:placing/aim
execute if score #rotation iyc.data matches 1 run setblock ~ ~ ~ minecraft:oak_fence_gate[facing=south]
execute if score #rotation iyc.data matches 2 run setblock ~ ~ ~ minecraft:oak_fence_gate[facing=west]
execute if score #rotation iyc.data matches 3 run setblock ~ ~ ~ minecraft:oak_fence_gate[facing=north]
execute if score #rotation iyc.data matches 4 run setblock ~ ~ ~ minecraft:oak_fence_gate[facing=east]
function iyc:shapes/gate_10

