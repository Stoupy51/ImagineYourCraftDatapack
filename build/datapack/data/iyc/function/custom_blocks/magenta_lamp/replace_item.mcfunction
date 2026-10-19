
#> iyc:custom_blocks/magenta_lamp/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1]
#
# @within	iyc:custom_blocks/magenta_lamp/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:structure_void"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.magenta_lamp.components
data modify entity @s Item.id set from storage iyc:items all.magenta_lamp.id

