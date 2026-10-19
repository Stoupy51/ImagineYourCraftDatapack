
#> iyc:custom_blocks/clear_glass/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:glass"}},distance=..1]
#
# @within	iyc:custom_blocks/clear_glass/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:glass"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.clear_glass.components
data modify entity @s Item.id set from storage iyc:items all.clear_glass.id

