
#> iyc:custom_blocks/_groups/minecraft_oak_fence_gate
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_glowstone_fence_gate iyc.data matches 1.. if entity @s[tag=iyc.glowstone_fence_gate] run function iyc:custom_blocks/glowstone_fence_gate/destroy
execute if score #total_log_fence_gate iyc.data matches 1.. if entity @s[tag=iyc.log_fence_gate] run function iyc:custom_blocks/log_fence_gate/destroy
execute if score #total_stone_fence_gate iyc.data matches 1.. if entity @s[tag=iyc.stone_fence_gate] run function iyc:custom_blocks/stone_fence_gate/destroy
execute if score #total_iron_fence_gate iyc.data matches 1.. if entity @s[tag=iyc.iron_fence_gate] run function iyc:custom_blocks/iron_fence_gate/destroy

