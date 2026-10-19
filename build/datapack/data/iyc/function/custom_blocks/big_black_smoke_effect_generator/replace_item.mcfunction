
#> iyc:custom_blocks/big_black_smoke_effect_generator/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:cobblestone"}},distance=..1]
#
# @within	iyc:custom_blocks/big_black_smoke_effect_generator/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:cobblestone"}},distance=..1] ]
#

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.big_black_smoke_effect_generator.components
data modify entity @s Item.id set from storage iyc:items all.big_black_smoke_effect_generator.id

