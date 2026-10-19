
#> iyc:custom_blocks/flatware/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:tripwire"}},distance=..1]
#
# @within	iyc:custom_blocks/flatware/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:tripwire"}},distance=..1] ]
#			iyc:custom_blocks/flatware/foreign_drop
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.flatware.components
data modify entity @s Item.id set from storage iyc:items all.flatware.id

