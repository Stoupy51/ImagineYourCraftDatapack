
#> iyc:custom_blocks/transparent_light_block/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/transparent_light_block/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.transparent_light_block
tag @s add iyc.vanilla.minecraft_light

# Add a custom name
data merge entity @s {"CustomName": {"text": "Transparent Light Block"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:transparent_light_block"]
function iyc:custom_blocks/compute_brightness

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.transparent_light_block"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
function iyc:shapes/fixed_0

