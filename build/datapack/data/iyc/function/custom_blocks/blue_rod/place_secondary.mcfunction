
#> iyc:custom_blocks/blue_rod/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/blue_rod/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.blue_rod
tag @s add iyc.vanilla.minecraft_structure_void

# Add a custom name
data merge entity @s {"CustomName": {"text": "Blue Rod"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:blue_rod"]
function iyc:custom_blocks/compute_brightness

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:0.3f,height:1.0f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.blue_rod"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.solid_neighbour_14
data modify entity @s item.components."minecraft:custom_model_data" set value {colors:[3361970]}
function iyc:shapes/solid_neighbour_14

