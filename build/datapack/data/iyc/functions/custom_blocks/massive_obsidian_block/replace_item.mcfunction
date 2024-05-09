
#> iyc:custom_blocks/massive_obsidian_block/replace_item
#
# @within	iyc:custom_blocks/massive_obsidian_block/destroy
#

data modify entity @s Item.components set from storage iyc:items all.massive_obsidian_block.components
data modify entity @s Item.id set from storage iyc:items all.massive_obsidian_block.id

