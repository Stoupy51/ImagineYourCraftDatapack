
#> iyc:custom_blocks/topaz_ore/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/topaz_ore/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.topaz_ore
tag @s add iyc.vanilla.minecraft_polished_deepslate

# Add a custom name
data merge entity @s {"CustomName": {"text": "Topaz Ore"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:topaz_ore"]
function iyc:custom_blocks/compute_brightness

