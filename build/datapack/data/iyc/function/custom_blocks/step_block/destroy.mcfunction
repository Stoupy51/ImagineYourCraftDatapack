
#> iyc:custom_blocks/step_block/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_smooth_stone
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:smooth_stone"}},distance=..1] run function iyc:custom_blocks/step_block/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_smooth_stone iyc.data 1
scoreboard players remove #total_step_block iyc.data 1

# Kill the custom block entity
kill @s

