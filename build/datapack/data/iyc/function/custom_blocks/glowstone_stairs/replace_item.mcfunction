
#> iyc:custom_blocks/glowstone_stairs/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:oak_stairs"}},distance=..1]
#
# @within	iyc:custom_blocks/glowstone_stairs/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:oak_stairs"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.glowstone_stairs.components
data modify entity @s Item.id set from storage iyc:items all.glowstone_stairs.id

