
#> iyc:custom_blocks/black_flower/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_tripwire
#

execute as @n[type=item,nbt={Item:{id:"minecraft:string"}},distance=..1] run function iyc:custom_blocks/black_flower/foreign_drop

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:tripwire"}},distance=..1] run function iyc:custom_blocks/black_flower/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_tripwire iyc.data 1
scoreboard players remove #total_black_flower iyc.data 1

# Kill the custom block entity
kill @s

