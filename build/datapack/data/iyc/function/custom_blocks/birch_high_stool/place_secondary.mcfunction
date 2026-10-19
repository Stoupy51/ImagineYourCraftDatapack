
#> iyc:custom_blocks/birch_high_stool/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/birch_high_stool/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.birch_high_stool
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Birch High Stool"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:birch_high_stool"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["iyc.interaction","iyc.seat.88"]}
function iyc:shapes/fixed_0

