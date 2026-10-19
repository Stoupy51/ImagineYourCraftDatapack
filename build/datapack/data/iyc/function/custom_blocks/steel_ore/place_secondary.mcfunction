
#> iyc:custom_blocks/steel_ore/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/steel_ore/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.steel_ore
tag @s add iyc.vanilla.minecraft_polished_deepslate

# Add a custom name
data merge entity @s {"CustomName": {"text": "Steel Ore"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:steel_ore"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

