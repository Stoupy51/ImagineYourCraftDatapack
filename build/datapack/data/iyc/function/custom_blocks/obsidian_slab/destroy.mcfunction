
#> iyc:custom_blocks/obsidian_slab/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_stone_slab
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:stone_slab"}},distance=..1] run function iyc:custom_blocks/obsidian_slab/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_stone_slab iyc.data 1
scoreboard players remove #total_obsidian_slab iyc.data 1

# Kill the custom block entity
kill @s

