
#> iyc:custom_blocks/flatware/foreign_drop
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:string"}},distance=..1]
#
# @within	iyc:custom_blocks/flatware/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:string"}},distance=..1] ]
#

data modify entity @s Item.count set value 1
function iyc:custom_blocks/flatware/replace_item

