
#> iyc:custom_blocks/oak_log_slab/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:oak_slab"}},distance=..1]
#
# @within	iyc:custom_blocks/oak_log_slab/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:oak_slab"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.oak_log_slab.components
data modify entity @s Item.id set from storage iyc:items all.oak_log_slab.id

