
#> iyc:custom_blocks/stone_campfire/foreign_drop
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:charcoal"}},distance=..1]
#
# @within	iyc:custom_blocks/stone_campfire/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:charcoal"}},distance=..1] ]
#

data modify entity @s Item.count set value 1
function iyc:custom_blocks/stone_campfire/replace_item

