
#> iyc:custom_blocks/iron_ladder/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:ladder"}},distance=..1]
#
# @within	iyc:custom_blocks/iron_ladder/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:ladder"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.iron_ladder.components
data modify entity @s Item.id set from storage iyc:items all.iron_ladder.id

