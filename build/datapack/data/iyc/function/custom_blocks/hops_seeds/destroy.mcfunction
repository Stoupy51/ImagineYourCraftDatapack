
#> iyc:custom_blocks/hops_seeds/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_wheat
#

# Replace the item with the custom one
scoreboard players operation #growth_time iyc.data = @s iyc.growth_time
execute as @n[type=item,nbt={Item:{id:"minecraft:wheat"}},distance=..1] run function iyc:custom_blocks/hops_seeds/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_wheat iyc.data 1
scoreboard players remove #total_hops_seeds iyc.data 1

# Kill the custom block entity
kill @s

# Decrease the number of entities with minute tag
scoreboard players remove #minute_entities iyc.data 1

