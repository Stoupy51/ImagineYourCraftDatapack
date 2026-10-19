
#> iyc:custom_blocks/steel_ore/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},distance=..1]
#
# @within	iyc:custom_blocks/steel_ore/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},distance=..1] ]
#

execute if entity @p[distance=..8,gamemode=survival] unless items entity @p[distance=..8,gamemode=survival] weapon.mainhand #iyc:iron_tier_pickaxes run return run kill @s

# If silk touch applied
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.id set from storage iyc:items all.steel_ore.id
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.components set from storage iyc:items all.steel_ore.components

# Else, no silk touch
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.id set from storage iyc:items all.raw_steel.id
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.components set from storage iyc:items all.raw_steel.components

# Get item count in every case
execute store result entity @s Item.count byte 1 run scoreboard players get #item_count iyc.data

