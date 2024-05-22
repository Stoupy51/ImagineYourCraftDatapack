
#> iyc:custom_blocks/white_flower/replace_item
#
# @within	iyc:custom_blocks/white_flower/destroy
#

data modify entity @s Item.components set from storage iyc:items all.white_flower.components
data modify entity @s Item.id set from storage iyc:items all.white_flower.id

