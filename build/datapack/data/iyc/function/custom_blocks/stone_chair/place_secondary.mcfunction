
#> iyc:custom_blocks/stone_chair/place_secondary
#
# @executed	at @s
#
# @within	iyc:custom_blocks/stone_chair/place_main [ at @s ]
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.stone_chair
tag @s add iyc.vanilla.minecraft_barrier

# Add a custom name
data merge entity @s {"CustomName": {"text": "Stone Chair"}}

# Modify item display entity to match the custom block
item replace entity @s contents with minecraft:furnace[item_model="iyc:stone_chair"]
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
summon interaction ~ ~-0.5 ~ {width:1.01f,height:1.01f,response:true,Tags:["iyc.interaction","iyc.seat.50"]}
function iyc:shapes/facing_away_18

