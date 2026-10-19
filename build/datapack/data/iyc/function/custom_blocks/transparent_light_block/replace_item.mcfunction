
#> iyc:custom_blocks/transparent_light_block/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:light"}},distance=..1]
#
# @within	iyc:custom_blocks/transparent_light_block/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:light"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.transparent_light_block.components
data modify entity @s Item.id set from storage iyc:items all.transparent_light_block.id

