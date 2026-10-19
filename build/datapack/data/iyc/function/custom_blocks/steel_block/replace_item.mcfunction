
#> iyc:custom_blocks/steel_block/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:iron_block"}},distance=..1]
#
# @within	iyc:custom_blocks/steel_block/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:iron_block"}},distance=..1] ]
#

execute if entity @p[distance=..8,gamemode=survival] unless items entity @p[distance=..8,gamemode=survival] weapon.mainhand #iyc:iron_tier_pickaxes run return run kill @s

# Replace the item with the custom one
data modify entity @s Item.components set from storage iyc:items all.steel_block.components
data modify entity @s Item.id set from storage iyc:items all.steel_block.id

