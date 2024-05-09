
#> iyc:custom_blocks/black_flower/place_secondary
#
# @within	iyc:custom_blocks/black_flower/place_main
#

# Add convention and utils tags, and the custom block tag
tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add smithed.block
tag @s add iyc.custom_block
tag @s add iyc.black_flower
tag @s add iyc.vanilla.minecraft_structure_void

# Modify item display entity to match the custom block
item replace entity @s container.0 with deepslate[minecraft:custom_model_data=2015110]
data modify entity @s transformation.scale set value [1.002f,1.002f,1.002f]
data modify entity @s brightness set value {block:15,sky:15}

## Check if the block have rotation
# Furnace case
scoreboard players set #rotation iyc.data 0
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ furnace[facing=north] run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ furnace[facing=east] run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ furnace[facing=south] run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ furnace[facing=west] run data modify entity @s Rotation[0] set value 90.0f
# Iron trapdoor case
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ iron_trapdoor[facing=north] run data modify entity @s Rotation[0] set value 180.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ iron_trapdoor[facing=east] run data modify entity @s Rotation[0] set value 270.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ iron_trapdoor[facing=south] run data modify entity @s Rotation[0] set value 0.0f
execute if score #rotation iyc.data matches 0 store success score #rotation iyc.data if block ~ ~ ~ iron_trapdoor[facing=west] run data modify entity @s Rotation[0] set value 90.0f
# No more cases for now

execute store result entity @s Rotation[0] float 90 run random value 0..3
