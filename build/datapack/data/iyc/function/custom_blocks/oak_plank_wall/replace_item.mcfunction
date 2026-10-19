
#> iyc:custom_blocks/oak_plank_wall/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:cobblestone_wall"}},distance=..1]
#
# @within	iyc:custom_blocks/oak_plank_wall/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:cobblestone_wall"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.oak_plank_wall.components
data modify entity @s Item.id set from storage iyc:items all.oak_plank_wall.id

