
#> iyc:custom_blocks/_groups/minecraft_oak_trapdoor
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_stone_trapdoor iyc.data matches 1.. if entity @s[tag=iyc.stone_trapdoor] run function iyc:custom_blocks/stone_trapdoor/destroy
execute if score #total_glowstone_trapdoor iyc.data matches 1.. if entity @s[tag=iyc.glowstone_trapdoor] run function iyc:custom_blocks/glowstone_trapdoor/destroy

