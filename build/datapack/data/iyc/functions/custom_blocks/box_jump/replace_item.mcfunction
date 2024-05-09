
#> iyc:custom_blocks/box_jump/replace_item
#
# @within	iyc:custom_blocks/box_jump/destroy
#

data modify entity @s Item.components set from storage iyc:items all.box_jump.components
data modify entity @s Item.id set from storage iyc:items all.box_jump.id

