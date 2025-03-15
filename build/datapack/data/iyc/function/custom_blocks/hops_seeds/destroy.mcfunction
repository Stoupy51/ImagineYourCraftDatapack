
#> iyc:custom_blocks/hops_seeds/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_wheat
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:wheat"}},distance=..1] run function iyc:custom_blocks/hops_seeds/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_wheat iyc.data 1
scoreboard players remove #total_hops_seeds iyc.data 1

# Kill the custom block entity
kill @s

