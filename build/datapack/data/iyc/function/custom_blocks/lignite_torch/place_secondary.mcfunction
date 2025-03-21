
#> iyc:custom_blocks/lignite_torch/place_secondary
#
# @within	iyc:custom_blocks/lignite_torch/place_main
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.lignite_torch
tag @s add iyc.vanilla.minecraft_torch

# Add a custom name
data merge entity @s {"CustomName": {"text": "Lignite Torch","italic": false,"color": "white"}}


# Modify item display entity to match the custom block
item replace entity @s container.0 with minecraft:furnace[item_model="iyc:lignite_torch"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
data modify entity @s brightness set value {block:15,sky:15}

