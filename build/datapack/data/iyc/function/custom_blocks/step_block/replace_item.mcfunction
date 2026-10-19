
#> iyc:custom_blocks/step_block/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:smooth_stone"}},distance=..1]
#
# @within	iyc:custom_blocks/step_block/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:smooth_stone"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.step_block.components
data modify entity @s Item.id set from storage iyc:items all.step_block.id

