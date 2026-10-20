
#> iyc:custom_blocks/_groups/minecraft_cobblestone_wall
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_oak_log_wall iyc.data matches 1.. if entity @s[tag=iyc.oak_log_wall] run function iyc:custom_blocks/oak_log_wall/destroy
execute if score #total_stone_wall iyc.data matches 1.. if entity @s[tag=iyc.stone_wall] run function iyc:custom_blocks/stone_wall/destroy
execute if score #total_oak_plank_wall iyc.data matches 1.. if entity @s[tag=iyc.oak_plank_wall] run function iyc:custom_blocks/oak_plank_wall/destroy
execute if score #total_glowstone_wall iyc.data matches 1.. if entity @s[tag=iyc.glowstone_wall] run function iyc:custom_blocks/glowstone_wall/destroy
execute if score #total_slate_wall iyc.data matches 1.. if entity @s[tag=iyc.slate_wall] run function iyc:custom_blocks/slate_wall/destroy

