
#> iyc:custom_blocks/glowstone_pressure_plate/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:stone_pressure_plate"}},distance=..1]
#
# @within	iyc:custom_blocks/glowstone_pressure_plate/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:stone_pressure_plate"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.glowstone_pressure_plate.components
data modify entity @s Item.id set from storage iyc:items all.glowstone_pressure_plate.id

