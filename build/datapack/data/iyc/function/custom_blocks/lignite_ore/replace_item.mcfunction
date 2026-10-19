
#> iyc:custom_blocks/lignite_ore/replace_item
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},distance=..1]
#
# @within	iyc:custom_blocks/lignite_ore/destroy [ as @n[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},distance=..1] ]
#

# If silk touch applied
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.id set from storage iyc:items all.lignite_ore.id
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.components set from storage iyc:items all.lignite_ore.components

# Else, no silk touch
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.id set from storage iyc:items all.lignite.id
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.components set from storage iyc:items all.lignite.components
execute if score #is_silk_touch iyc.data matches 0 summon minecraft:experience_orb store result entity @s Value short 1 run random value 2..5

# Get item count in every case
execute store result entity @s Item.count byte 1 run scoreboard players get #item_count iyc.data

