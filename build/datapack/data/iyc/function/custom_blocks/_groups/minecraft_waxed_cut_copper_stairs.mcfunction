
#> iyc:custom_blocks/_groups/minecraft_waxed_cut_copper_stairs
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_iron_stairs iyc.data matches 1.. if entity @s[tag=iyc.iron_stairs] run function iyc:custom_blocks/iron_stairs/destroy

