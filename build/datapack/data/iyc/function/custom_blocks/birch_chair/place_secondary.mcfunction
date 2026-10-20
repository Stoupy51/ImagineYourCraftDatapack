
#> iyc:custom_blocks/birch_chair/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/birch_chair/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.birch_chair
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Birch Chair"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:birch_chair"]
function iyc:custom_blocks/compute_brightness

# Apply rotation
execute if score #rotation iyc.data matches 1 run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 2 run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 3 run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 4 run data modify entity @s Rotation[0] set value 90.0f

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.birch_chair"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
function iyc:shapes/facing_away_18

