
#> iyc:custom_blocks/gray_lit_lamp/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:light"}},distance=..1]
#
# @within	iyc:custom_blocks/gray_lit_lamp/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:light"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.gray_lit_lamp.components
data modify entity @s Item.id set from storage iyc:items all.gray_lit_lamp.id

