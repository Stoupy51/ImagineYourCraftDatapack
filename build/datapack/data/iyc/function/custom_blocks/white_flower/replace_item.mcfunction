
#> iyc:custom_blocks/white_flower/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:tripwire"}},distance=..1]
#
# @within	iyc:custom_blocks/white_flower/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:tripwire"}},distance=..1] ]
#			iyc:custom_blocks/white_flower/foreign_drop
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.white_flower.components
data modify entity @s Item.id set from storage iyc:items all.white_flower.id

