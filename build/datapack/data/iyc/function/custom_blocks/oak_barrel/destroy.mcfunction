
#> iyc:custom_blocks/oak_barrel/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_barrel
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:barrel"}},distance=..1] run function iyc:custom_blocks/oak_barrel/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_barrel iyc.data 1
scoreboard players remove #total_oak_barrel iyc.data 1

# Kill the custom block entity
kill @s

