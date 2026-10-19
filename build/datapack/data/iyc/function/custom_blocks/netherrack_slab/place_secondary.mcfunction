
#> iyc:custom_blocks/netherrack_slab/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/netherrack_slab/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.netherrack_slab
tag @s add iyc.vanilla.minecraft_nether_brick_slab

# Add a custom name
data merge entity @s {"CustomName": {"text": "Netherrack Slab"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:netherrack_slab"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.slab_4
function iyc:placing/aim
execute if score #upper iyc.data matches 1 run setblock ~ ~ ~ minecraft:nether_brick_slab[type=top]
function iyc:shapes/slab_4

