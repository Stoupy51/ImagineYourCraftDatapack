
#> iyc:custom_blocks/iron_furnace/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/iron_furnace/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.iron_furnace
tag @s add iyc.vanilla.minecraft_furnace

# Add a custom name
data merge entity @s {"CustomName": {"text": "Iron Furnace"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:iron_furnace"]
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
tag @s add iyc.tree.furnace_21
function iyc:shapes/furnace_21

# Add tag for loop every tick
tag @s add iyc.tick
scoreboard players add #tick_entities iyc.data 1

