
#> iyc:custom_blocks/oak_table/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_table/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.oak_table
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Oak Table"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:oak_table"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.same_neighbour_15
tag @s add iyc.connect.table
summon interaction ~ ~-0.5 ~ {width:1.01f,height:0.85f,response:true,Tags:["iyc.interaction"]}
function iyc:shapes/same_neighbour_15

