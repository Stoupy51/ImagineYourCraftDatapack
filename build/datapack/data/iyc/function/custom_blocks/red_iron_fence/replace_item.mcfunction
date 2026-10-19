
#> iyc:custom_blocks/red_iron_fence/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:nether_brick_fence"}},distance=..1]
#
# @within	iyc:custom_blocks/red_iron_fence/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:nether_brick_fence"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.red_iron_fence.components
data modify entity @s Item.id set from storage iyc:items all.red_iron_fence.id

