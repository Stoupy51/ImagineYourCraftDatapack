
#> iyc:custom_blocks/birch_log_slopes/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/birch_log_slopes/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.birch_log_slopes
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Birch Log Slopes"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:birch_log_slopes"]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
function iyc:custom_blocks/compute_brightness

# Apply rotation
execute if score #rotation iyc.data matches 1 run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 2 run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 3 run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 4 run data modify entity @s Rotation[0] set value 90.0f

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.step
function iyc:placing/aim
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["iyc.interaction"]}
function iyc:shapes/slope_2

