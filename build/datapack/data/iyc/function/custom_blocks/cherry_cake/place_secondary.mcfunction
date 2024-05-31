
#> iyc:custom_blocks/cherry_cake/place_secondary
#
# @within	iyc:custom_blocks/cherry_cake/place_main
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.cherry_cake
tag @s add iyc.vanilla.minecraft_cake

# Modify item display entity to match the custom block
item replace entity @s container.0 with minecraft:furnace[minecraft:custom_model_data=2015129]
data modify entity @s transformation.scale set value [1.002f,1.008f,1.002f]
data modify entity @s transformation.translation[1] set value 0.003f
data modify entity @s brightness set value {block:15,sky:15}

