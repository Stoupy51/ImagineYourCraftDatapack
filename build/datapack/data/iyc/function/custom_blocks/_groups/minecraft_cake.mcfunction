
#> iyc:custom_blocks/_groups/minecraft_cake
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_cherry_cake iyc.data matches 1.. if entity @s[tag=iyc.cherry_cake] run function iyc:custom_blocks/cherry_cake/destroy

