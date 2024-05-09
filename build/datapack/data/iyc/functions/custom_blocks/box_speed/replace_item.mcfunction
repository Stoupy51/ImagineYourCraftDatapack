
#> iyc:custom_blocks/box_speed/replace_item
#
# @within	iyc:custom_blocks/box_speed/destroy
#

data modify entity @s Item.components set from storage iyc:items all.box_speed.components
data modify entity @s Item.id set from storage iyc:items all.box_speed.id

