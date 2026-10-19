
#> iyc:custom_blocks/_groups/minecraft_oak_slab
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_reversed_planks_slab iyc.data matches 1.. if entity @s[tag=iyc.reversed_planks_slab] run function iyc:custom_blocks/reversed_planks_slab/destroy
execute if score #total_oak_log_slab iyc.data matches 1.. if entity @s[tag=iyc.oak_log_slab] run function iyc:custom_blocks/oak_log_slab/destroy
execute if score #total_glowstone_slab iyc.data matches 1.. if entity @s[tag=iyc.glowstone_slab] run function iyc:custom_blocks/glowstone_slab/destroy

