
#> iyc:custom_blocks/lignite_torch/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:torch"}},distance=..1]
#
# @within	iyc:custom_blocks/lignite_torch/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:torch"}},distance=..1] ]
#			iyc:custom_blocks/lignite_wall_torch/foreign_drop
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.lignite_torch.components
data modify entity @s Item.id set from storage iyc:items all.lignite_torch.id

