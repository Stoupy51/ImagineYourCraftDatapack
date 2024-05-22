
#> iyc:custom_blocks/cloud/replace_item
#
# @within	iyc:custom_blocks/cloud/destroy
#

data modify entity @s Item.components set from storage iyc:items all.cloud.components
data modify entity @s Item.id set from storage iyc:items all.cloud.id

