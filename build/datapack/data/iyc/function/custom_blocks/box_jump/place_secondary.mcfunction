
#> iyc:custom_blocks/box_jump/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/box_jump/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.box_jump
tag @s add iyc.vanilla.minecraft_oak_planks

# Add a custom name
data merge entity @s {"CustomName": {"text": "Box Jump"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:box_jump"]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.jump_box
function iyc:shapes/fixed_0

# Add tag for loop every tick
tag @s add iyc.tick
scoreboard players add #tick_entities iyc.data 1

