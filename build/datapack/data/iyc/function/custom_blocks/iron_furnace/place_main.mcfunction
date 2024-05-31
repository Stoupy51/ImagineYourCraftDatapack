
#> iyc:custom_blocks/iron_furnace/place_main
#
# @within	iyc:custom_blocks/place
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
execute if predicate iyc:facing/north run setblock ~ ~ ~ minecraft:furnace[facing=north,]
execute if predicate iyc:facing/east run setblock ~ ~ ~ minecraft:furnace[facing=east,]
execute if predicate iyc:facing/south run setblock ~ ~ ~ minecraft:furnace[facing=south,]
execute if predicate iyc:facing/west run setblock ~ ~ ~ minecraft:furnace[facing=west,]
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/iron_furnace/place_secondary
tag @s remove iyc.placer

