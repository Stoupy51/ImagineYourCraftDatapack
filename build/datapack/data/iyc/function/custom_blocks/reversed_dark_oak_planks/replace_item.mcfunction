
#> iyc:custom_blocks/reversed_dark_oak_planks/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:dark_oak_planks"}},distance=..1]
#
# @within	iyc:custom_blocks/reversed_dark_oak_planks/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:dark_oak_planks"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.reversed_dark_oak_planks.components
data modify entity @s Item.id set from storage iyc:items all.reversed_dark_oak_planks.id

