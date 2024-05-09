
#> iyc:custom_blocks/iron_ladder/place_main
#
# @within	???
#

execute if block ~ ~ ~ minecraft:furnace[facing=north] run setblock ~ ~ ~ minecraft:ladder[facing=north]
execute if block ~ ~ ~ minecraft:furnace[facing=south] run setblock ~ ~ ~ minecraft:ladder[facing=south]
execute if block ~ ~ ~ minecraft:furnace[facing=west] run setblock ~ ~ ~ minecraft:ladder[facing=west]
execute if block ~ ~ ~ minecraft:furnace[facing=east] run setblock ~ ~ ~ minecraft:ladder[facing=east]
execute align xyz positioned ~.5 ~.5 ~.5 summon item_display at @s run function iyc:custom_blocks/iron_ladder/place_secondary

