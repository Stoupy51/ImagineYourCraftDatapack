
#> iyc:custom_blocks/iron_lantern/replace_item
#
# @within	iyc:custom_blocks/iron_lantern/destroy
#

data modify entity @s Item.components set from storage iyc:items all.iron_lantern.components
data modify entity @s Item.id set from storage iyc:items all.iron_lantern.id

