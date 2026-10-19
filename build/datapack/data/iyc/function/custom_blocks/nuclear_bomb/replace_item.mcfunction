
#> iyc:custom_blocks/nuclear_bomb/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:tnt"}},distance=..1]
#
# @within	iyc:custom_blocks/nuclear_bomb/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:tnt"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.nuclear_bomb.components
data modify entity @s Item.id set from storage iyc:items all.nuclear_bomb.id

