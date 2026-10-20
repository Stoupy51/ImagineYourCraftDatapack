
#> iyc:custom_blocks/slate_block/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:emerald_block"}},distance=..1]
#
# @within	iyc:custom_blocks/slate_block/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:emerald_block"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.slate_block.components
data modify entity @s Item.id set from storage iyc:items all.slate_block.id

