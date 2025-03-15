
#> iyc:custom_blocks/cloud/place_secondary
#
# @within	iyc:custom_blocks/cloud/place_main
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.cloud
tag @s add iyc.vanilla.minecraft_structure_void

# Add a custom name
data merge entity @s {"CustomName": {"text": "Cloud","italic": false,"color": "white"}}


# Modify item display entity to match the custom block
item replace entity @s container.0 with minecraft:furnace[item_model="iyc:cloud"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
data modify entity @s brightness set value {block:15,sky:15}

