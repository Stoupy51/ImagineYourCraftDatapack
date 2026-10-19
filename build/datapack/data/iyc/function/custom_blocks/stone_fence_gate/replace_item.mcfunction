
#> iyc:custom_blocks/stone_fence_gate/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:oak_fence_gate"}},distance=..1]
#
# @within	iyc:custom_blocks/stone_fence_gate/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:oak_fence_gate"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.stone_fence_gate.components
data modify entity @s Item.id set from storage iyc:items all.stone_fence_gate.id

