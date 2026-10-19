
#> iyc:custom_blocks/red_lamp/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1]
#
# @within	iyc:custom_blocks/red_lamp/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.red_lamp.components
data modify entity @s Item.id set from storage iyc:items all.red_lamp.id

