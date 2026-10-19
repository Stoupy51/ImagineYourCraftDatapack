
#> iyc:custom_blocks/glowstone_stairs/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_stairs/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.glowstone_stairs
tag @s add iyc.vanilla.minecraft_oak_stairs

# Add a custom name
data merge entity @s {"CustomName": {"text": "Glowstone Stairs"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:glowstone_stairs"]
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
tag @s add iyc.tree.stairs_1
function iyc:placing/aim
execute if score #rotation iyc.data matches 1 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:oak_stairs[facing=south,half=bottom]
execute if score #rotation iyc.data matches 1 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:oak_stairs[facing=south,half=top]
execute if score #rotation iyc.data matches 2 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:oak_stairs[facing=west,half=bottom]
execute if score #rotation iyc.data matches 2 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:oak_stairs[facing=west,half=top]
execute if score #rotation iyc.data matches 3 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:oak_stairs[facing=north,half=bottom]
execute if score #rotation iyc.data matches 3 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:oak_stairs[facing=north,half=top]
execute if score #rotation iyc.data matches 4 if score #upper iyc.data matches 0 run setblock ~ ~ ~ minecraft:oak_stairs[facing=east,half=bottom]
execute if score #rotation iyc.data matches 4 if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:oak_stairs[facing=east,half=top]
function iyc:shapes/stairs_1

# Add tag for loop every second
tag @s add iyc.second
scoreboard players add #second_entities iyc.data 1

