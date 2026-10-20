
#> iyc:custom_blocks/_groups/minecraft_nether_brick_slab
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_netherrack_slab iyc.data matches 1.. if entity @s[tag=iyc.netherrack_slab] run function iyc:custom_blocks/netherrack_slab/destroy

