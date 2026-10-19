
#> iyc:custom_blocks/iron_stairs/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:waxed_cut_copper_stairs"}},distance=..1]
#
# @within	iyc:custom_blocks/iron_stairs/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:waxed_cut_copper_stairs"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.iron_stairs.components
data modify entity @s Item.id set from storage iyc:items all.iron_stairs.id

