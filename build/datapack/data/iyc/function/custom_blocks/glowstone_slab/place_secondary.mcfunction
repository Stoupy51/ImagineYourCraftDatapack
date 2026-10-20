
#> iyc:custom_blocks/glowstone_slab/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/glowstone_slab/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.glowstone_slab
tag @s add iyc.vanilla.minecraft_oak_slab

# Add a custom name
data merge entity @s {"CustomName": {"text": "Glowstone Slab"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:glowstone_slab"]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.slab_4
function iyc:shapes/slab_4

