
#> iyc:custom_blocks/cherry_cake/replace_item
#
# @within	iyc:custom_blocks/cherry_cake/destroy
#

data modify entity @s Item.components set from storage iyc:items all.cherry_cake.components
data modify entity @s Item.id set from storage iyc:items all.cherry_cake.id

