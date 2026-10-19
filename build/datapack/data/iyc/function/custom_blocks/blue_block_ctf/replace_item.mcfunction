
#> iyc:custom_blocks/blue_block_ctf/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:glass"}},distance=..1]
#
# @within	iyc:custom_blocks/blue_block_ctf/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:glass"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.blue_block_ctf.components
data modify entity @s Item.id set from storage iyc:items all.blue_block_ctf.id

