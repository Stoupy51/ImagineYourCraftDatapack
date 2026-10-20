
#> iyc:custom_blocks/steel_block/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:gold_block"}},distance=..1]
#
# @within	iyc:custom_blocks/steel_block/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:gold_block"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.steel_block.components
data modify entity @s Item.id set from storage iyc:items all.steel_block.id

