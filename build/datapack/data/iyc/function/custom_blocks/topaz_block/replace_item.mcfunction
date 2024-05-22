
#> iyc:custom_blocks/topaz_block/replace_item
#
# @within	iyc:custom_blocks/topaz_block/destroy
#

data modify entity @s Item.components set from storage iyc:items all.topaz_block.components
data modify entity @s Item.id set from storage iyc:items all.topaz_block.id

