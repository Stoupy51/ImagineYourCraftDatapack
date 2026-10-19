
#> iyc:custom_blocks/oak_log_wall/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_cobblestone_wall
#

execute unless entity @n[type=item,nbt={Item:{id:"minecraft:cobblestone_wall"}},distance=..1] if entity @p[distance=..8,gamemode=survival] run loot spawn ~ ~ ~ loot iyc:i/oak_log_wall

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:cobblestone_wall"}},distance=..1] run function iyc:custom_blocks/oak_log_wall/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_cobblestone_wall iyc.data 1
scoreboard players remove #total_oak_log_wall iyc.data 1

# Kill the custom block entity
kill @s

