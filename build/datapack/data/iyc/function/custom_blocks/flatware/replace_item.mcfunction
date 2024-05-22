
#> iyc:custom_blocks/flatware/replace_item
#
# @within	iyc:custom_blocks/flatware/destroy
#

data modify entity @s Item.components set from storage iyc:items all.flatware.components
data modify entity @s Item.id set from storage iyc:items all.flatware.id

