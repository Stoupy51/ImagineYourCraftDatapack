
#> iyc:custom_blocks/hops_seeds/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:wheat"}},distance=..1]
#
# @within	iyc:custom_blocks/hops_seeds/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:wheat"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.hops_seeds.components
data modify entity @s Item.id set from storage iyc:items all.hops_seeds.id

# Check if the seed is fully grown
function iyc:custom_blocks/hops_seeds/is_fully_grown

