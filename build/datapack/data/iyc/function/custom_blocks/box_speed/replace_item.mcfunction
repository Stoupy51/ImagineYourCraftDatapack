
#> iyc:custom_blocks/box_speed/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:oak_planks"}},distance=..1]
#
# @within	iyc:custom_blocks/box_speed/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:oak_planks"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.box_speed.components
data modify entity @s Item.id set from storage iyc:items all.box_speed.id

