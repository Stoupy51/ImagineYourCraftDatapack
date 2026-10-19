
#> iyc:custom_blocks/brown_cloud/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1]
#
# @within	iyc:custom_blocks/brown_cloud/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.brown_cloud.components
data modify entity @s Item.id set from storage iyc:items all.brown_cloud.id

