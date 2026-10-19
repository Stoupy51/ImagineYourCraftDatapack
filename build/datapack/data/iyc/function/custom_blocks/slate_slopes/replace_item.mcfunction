
#> iyc:custom_blocks/slate_slopes/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:barrier"}},distance=..1]
#
# @within	iyc:custom_blocks/slate_slopes/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:barrier"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.slate_slopes.components
data modify entity @s Item.id set from storage iyc:items all.slate_slopes.id

