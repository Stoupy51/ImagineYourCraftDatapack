
#> iyc:custom_blocks/hops_seeds/is_fully_grown
#
# @executed	as @n[type=item,nbt={Item:{id:"minecraft:wheat"}},distance=..1]
#
# @within	iyc:custom_blocks/hops_seeds/replace_item
#

# If fully grown, drop the loot table and kill the current entity (item)
execute if score #growth_time iyc.data matches 480.. as @p[gamemode=!spectator] run loot spawn ~ ~ ~ fish iyc:seeds/hops ~ ~ ~ mainhand
execute if score #growth_time iyc.data matches 480.. run kill @s

