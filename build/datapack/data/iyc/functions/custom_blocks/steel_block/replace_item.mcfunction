
#> iyc:custom_blocks/steel_block/replace_item
#
# @within	iyc:custom_blocks/steel_block/destroy
#

data modify entity @s Item.components set from storage iyc:items all.steel_block.components
data modify entity @s Item.id set from storage iyc:items all.steel_block.id

