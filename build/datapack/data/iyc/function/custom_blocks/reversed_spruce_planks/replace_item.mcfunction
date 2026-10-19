
#> iyc:custom_blocks/reversed_spruce_planks/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:spruce_planks"}},distance=..1]
#
# @within	iyc:custom_blocks/reversed_spruce_planks/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:spruce_planks"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.reversed_spruce_planks.components
data modify entity @s Item.id set from storage iyc:items all.reversed_spruce_planks.id

