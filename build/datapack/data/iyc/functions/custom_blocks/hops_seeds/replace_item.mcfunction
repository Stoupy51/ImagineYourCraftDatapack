
#> iyc:custom_blocks/hops_seeds/replace_item
#
# @within	iyc:custom_blocks/hops_seeds/destroy
#

data modify entity @s Item.components set from storage iyc:items all.hops_seeds.components
data modify entity @s Item.id set from storage iyc:items all.hops_seeds.id

