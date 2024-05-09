
#> iyc:custom_blocks/iron_ladder/replace_item
#
# @within	iyc:custom_blocks/iron_ladder/destroy
#

data modify entity @s Item.components set from storage iyc:items all.iron_ladder.components
data modify entity @s Item.id set from storage iyc:items all.iron_ladder.id

