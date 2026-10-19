
#> iyc:custom_blocks/_groups/minecraft_smooth_stone
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_step_block iyc.data matches 1.. if entity @s[tag=iyc.step_block] run function iyc:custom_blocks/step_block/destroy

