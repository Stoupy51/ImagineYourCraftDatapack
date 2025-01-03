
#> iyc:custom_blocks/iron_furnace/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air
execute if score #rotation iyc.data matches 1 run setblock ~ ~ ~ minecraft:furnace[facing=north]{"CustomName": "{\"text\": \"Iron Furnace\", \"italic\": false, \"color\": \"white\"}"}
execute if score #rotation iyc.data matches 2 run setblock ~ ~ ~ minecraft:furnace[facing=east]{"CustomName": "{\"text\": \"Iron Furnace\", \"italic\": false, \"color\": \"white\"}"}
execute if score #rotation iyc.data matches 3 run setblock ~ ~ ~ minecraft:furnace[facing=south]{"CustomName": "{\"text\": \"Iron Furnace\", \"italic\": false, \"color\": \"white\"}"}
execute if score #rotation iyc.data matches 4 run setblock ~ ~ ~ minecraft:furnace[facing=west]{"CustomName": "{\"text\": \"Iron Furnace\", \"italic\": false, \"color\": \"white\"}"}
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/iron_furnace/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_furnace iyc.data 1
scoreboard players add #total_iron_furnace iyc.data 1

