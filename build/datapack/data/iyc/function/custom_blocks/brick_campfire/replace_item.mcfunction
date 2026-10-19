
#> iyc:custom_blocks/brick_campfire/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:campfire"}},distance=..1]
#
# @within	iyc:custom_blocks/brick_campfire/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:campfire"}},distance=..1] ]
#			iyc:custom_blocks/brick_campfire/foreign_drop
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.brick_campfire.components
data modify entity @s Item.id set from storage iyc:items all.brick_campfire.id

