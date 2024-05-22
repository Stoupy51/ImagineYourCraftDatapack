
#> iyc:custom_blocks/iron_furnace/replace_item
#
# @within	iyc:custom_blocks/iron_furnace/destroy
#

data modify entity @s Item.components set from storage iyc:items all.iron_furnace.components
data modify entity @s Item.id set from storage iyc:items all.iron_furnace.id

