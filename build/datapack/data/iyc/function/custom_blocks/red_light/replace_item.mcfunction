
#> iyc:custom_blocks/red_light/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:redstone_lamp"}},distance=..1]
#
# @within	iyc:custom_blocks/red_light/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:redstone_lamp"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.red_light.components
data modify entity @s Item.id set from storage iyc:items all.red_light.id

