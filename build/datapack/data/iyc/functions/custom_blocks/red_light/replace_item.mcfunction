
#> iyc:custom_blocks/red_light/replace_item
#
# @within	iyc:custom_blocks/red_light/destroy
#

data modify entity @s Item.components set from storage iyc:items all.red_light.components
data modify entity @s Item.id set from storage iyc:items all.red_light.id

