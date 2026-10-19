
#> iyc:custom_blocks/lignite_wall_torch/place_main
#
# @within	iyc:custom_blocks/lignite_torch/place_main
#			iyc:custom_blocks/place
#			iyc:interaction/light
#

tag @s add iyc.placer
function iyc:custom_blocks/get_rotation
setblock ~ ~ ~ air strict
execute if score #rotation iyc.data matches 1 run setblock ~ ~ ~ minecraft:wall_torch[facing=north]
execute if score #rotation iyc.data matches 2 run setblock ~ ~ ~ minecraft:wall_torch[facing=east]
execute if score #rotation iyc.data matches 3 run setblock ~ ~ ~ minecraft:wall_torch[facing=south]
execute if score #rotation iyc.data matches 4 run setblock ~ ~ ~ minecraft:wall_torch[facing=west]
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/lignite_wall_torch/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_wall_torch iyc.data 1
scoreboard players add #total_lignite_wall_torch iyc.data 1

