
#> iyc:custom_blocks/blob/replace_item
#
# @within	iyc:custom_blocks/blob/destroy
#

data modify entity @s Item.components set from storage iyc:items all.blob.components
data modify entity @s Item.id set from storage iyc:items all.blob.id

