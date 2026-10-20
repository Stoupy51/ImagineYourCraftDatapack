
#> iyc:custom_blocks/sandstone_slopes/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/sandstone_slopes/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.sandstone_slopes
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Sandstone Slopes"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:sandstone_slopes"]
function iyc:custom_blocks/compute_brightness

# Apply rotation
execute if score #rotation iyc.data matches 1 run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 2 run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 3 run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 4 run data modify entity @s Rotation[0] set value 90.0f

# Interaction breaking the block when hit
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["global.ignore","global.ignore.kill","smithed.entity","iyc.interaction","iyc.sandstone_slopes"]}

# Original model
tag @s add iyc.original
scoreboard players set @s iyc.shape -1
tag @s add iyc.step
execute summon marker run function iyc:custom_blocks/_aim/main
function iyc:shapes/slope_2

