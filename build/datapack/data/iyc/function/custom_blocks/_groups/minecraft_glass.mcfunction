
#> iyc:custom_blocks/_groups/minecraft_glass
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_blue_block_ctf iyc.data matches 1.. if entity @s[tag=iyc.blue_block_ctf] run function iyc:custom_blocks/blue_block_ctf/destroy

