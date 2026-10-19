
#> iyc:custom_blocks/oak_reversed_planks_stairs/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:oak_stairs"}},distance=..1]
#
# @within	iyc:custom_blocks/oak_reversed_planks_stairs/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:oak_stairs"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.oak_reversed_planks_stairs.components
data modify entity @s Item.id set from storage iyc:items all.oak_reversed_planks_stairs.id

