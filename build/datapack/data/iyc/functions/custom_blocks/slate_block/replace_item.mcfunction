
#> iyc:custom_blocks/slate_block/replace_item
#
# @within	iyc:custom_blocks/slate_block/destroy
#

data modify entity @s Item.components set from storage iyc:items all.slate_block.components
data modify entity @s Item.id set from storage iyc:items all.slate_block.id

