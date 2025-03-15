
#> iyc:custom_blocks/massive_obsidian_block/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_netherite_block
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:netherite_block"}},distance=..1] run function iyc:custom_blocks/massive_obsidian_block/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_netherite_block iyc.data 1
scoreboard players remove #total_massive_obsidian_block iyc.data 1

# Kill the custom block entity
kill @s

