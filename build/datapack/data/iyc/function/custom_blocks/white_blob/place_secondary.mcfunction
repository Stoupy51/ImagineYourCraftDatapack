
#> iyc:custom_blocks/white_blob/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/white_blob/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.white_blob
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "White Blob"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:white_blob"]
function iyc:custom_blocks/compute_brightness

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.white_blob"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
data modify entity @s item.components."minecraft:custom_model_data" set value {colors:[16777215]}
function iyc:shapes/fixed_0

