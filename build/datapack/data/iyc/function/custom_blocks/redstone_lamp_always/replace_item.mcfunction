
#> iyc:custom_blocks/redstone_lamp_always/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:ochre_froglight"}},distance=..1]
#
# @within	iyc:custom_blocks/redstone_lamp_always/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:ochre_froglight"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.redstone_lamp_always.components
data modify entity @s Item.id set from storage iyc:items all.redstone_lamp_always.id

