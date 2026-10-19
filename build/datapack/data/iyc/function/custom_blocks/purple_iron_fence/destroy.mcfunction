
#> iyc:custom_blocks/purple_iron_fence/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_nether_brick_fence
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:nether_brick_fence"}},distance=..1] run function iyc:custom_blocks/purple_iron_fence/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_nether_brick_fence iyc.data 1
scoreboard players remove #total_purple_iron_fence iyc.data 1

# Kill the custom block entity
kill @s

