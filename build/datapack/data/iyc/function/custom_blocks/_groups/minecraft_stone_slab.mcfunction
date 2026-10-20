
#> iyc:custom_blocks/_groups/minecraft_stone_slab
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_obsidian_slab iyc.data matches 1.. if entity @s[tag=iyc.obsidian_slab] run function iyc:custom_blocks/obsidian_slab/destroy
execute if score #total_slate_slab iyc.data matches 1.. if entity @s[tag=iyc.slate_slab] run function iyc:custom_blocks/slate_slab/destroy

