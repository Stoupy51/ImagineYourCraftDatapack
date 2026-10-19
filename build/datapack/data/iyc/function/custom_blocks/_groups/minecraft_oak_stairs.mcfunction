
#> iyc:custom_blocks/_groups/minecraft_oak_stairs
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_log_stairs iyc.data matches 1.. if entity @s[tag=iyc.log_stairs] run function iyc:custom_blocks/log_stairs/destroy
execute if score #total_glowstone_stairs iyc.data matches 1.. if entity @s[tag=iyc.glowstone_stairs] run function iyc:custom_blocks/glowstone_stairs/destroy
execute if score #total_oak_reversed_planks_stairs iyc.data matches 1.. if entity @s[tag=iyc.oak_reversed_planks_stairs] run function iyc:custom_blocks/oak_reversed_planks_stairs/destroy

