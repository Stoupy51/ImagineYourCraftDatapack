
#> iyc:custom_blocks/slate_wall/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_cobblestone_wall
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:cobblestone_wall"}},distance=..1] run function iyc:custom_blocks/slate_wall/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_cobblestone_wall iyc.data 1
scoreboard players remove #total_slate_wall iyc.data 1

# Kill the custom block entity
kill @s

