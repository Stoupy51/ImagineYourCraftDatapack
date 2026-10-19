
#> iyc:custom_blocks/_groups/minecraft_wall_torch
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_lignite_wall_torch iyc.data matches 1.. if entity @s[tag=iyc.lignite_wall_torch] run function iyc:custom_blocks/lignite_wall_torch/destroy

