
#> iyc:custom_blocks/orange_lit_lamp/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/orange_lit_lamp/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.orange_lit_lamp
tag @s add iyc.vanilla.minecraft_light

# Add a custom name
data merge entity @s {"CustomName": {"text": "Orange Lit Lamp"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:orange_lit_lamp"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.solid_neighbour_14
data modify entity @s item.components."minecraft:custom_model_data" set value {colors:[14188339]}
summon interaction ~ ~-0.5 ~ {width:0.6f,height:0.8f,response:true,Tags:["iyc.interaction"]}
function iyc:shapes/solid_neighbour_14

