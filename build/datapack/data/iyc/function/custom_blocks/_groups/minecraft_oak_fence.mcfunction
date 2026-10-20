
#> iyc:custom_blocks/_groups/minecraft_oak_fence
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_glowstone_fence iyc.data matches 1.. if entity @s[tag=iyc.glowstone_fence] run function iyc:custom_blocks/glowstone_fence/destroy
execute if score #total_log_fence iyc.data matches 1.. if entity @s[tag=iyc.log_fence] run function iyc:custom_blocks/log_fence/destroy

