
#> iyc:custom_blocks/iron_ladder/place_main
#
# @within	???
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
execute if predicate iyc:facing/north run setblock ~ ~ ~ minecraft:ladder[facing=north,]
execute if predicate iyc:facing/east run setblock ~ ~ ~ minecraft:ladder[facing=east,]
execute if predicate iyc:facing/south run setblock ~ ~ ~ minecraft:ladder[facing=south,]
execute if predicate iyc:facing/west run setblock ~ ~ ~ minecraft:ladder[facing=west,]
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/iron_ladder/place_secondary
tag @s remove iyc.placer

