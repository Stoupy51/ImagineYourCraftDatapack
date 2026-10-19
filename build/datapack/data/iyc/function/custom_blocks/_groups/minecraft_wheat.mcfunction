
#> iyc:custom_blocks/_groups/minecraft_wheat
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_hops_seeds iyc.data matches 1.. if entity @s[tag=iyc.hops_seeds] run function iyc:custom_blocks/hops_seeds/destroy

