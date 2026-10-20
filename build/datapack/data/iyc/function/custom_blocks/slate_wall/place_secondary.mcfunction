
#> iyc:custom_blocks/slate_wall/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/slate_wall/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.slate_wall
tag @s add iyc.vanilla.minecraft_cobblestone_wall

# Add a custom name
data merge entity @s {"CustomName": {"text": "Slate Wall"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:slate_wall"]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.wall_8
function iyc:shapes/wall_8

