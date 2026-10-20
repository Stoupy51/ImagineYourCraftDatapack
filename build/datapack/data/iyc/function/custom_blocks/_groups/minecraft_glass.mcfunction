
#> iyc:custom_blocks/_groups/minecraft_glass
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_clear_glass iyc.data matches 1.. if entity @s[tag=iyc.clear_glass] run function iyc:custom_blocks/clear_glass/destroy
execute if score #total_blue_block_ctf iyc.data matches 1.. if entity @s[tag=iyc.blue_block_ctf] run function iyc:custom_blocks/blue_block_ctf/destroy
execute if score #total_red_block_ctf iyc.data matches 1.. if entity @s[tag=iyc.red_block_ctf] run function iyc:custom_blocks/red_block_ctf/destroy

