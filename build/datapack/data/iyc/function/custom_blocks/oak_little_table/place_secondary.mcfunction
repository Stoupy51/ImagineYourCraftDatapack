
#> iyc:custom_blocks/oak_little_table/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/oak_little_table/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.oak_little_table
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Oak Little Table"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:oak_little_table"]
function iyc:custom_blocks/compute_brightness

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:1.01f,height:0.38f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.oak_little_table"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.follow
tag @s add iyc.tree.same_neighbour_16
tag @s add iyc.connect.little_table
function iyc:shapes/same_neighbour_16

