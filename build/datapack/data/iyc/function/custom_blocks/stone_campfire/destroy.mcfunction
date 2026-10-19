
#> iyc:custom_blocks/stone_campfire/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_campfire
#

execute as @n[type=item,nbt={Item:{id:"minecraft:charcoal"}},distance=..1] run function iyc:custom_blocks/stone_campfire/foreign_drop

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:campfire"}},distance=..1] run function iyc:custom_blocks/stone_campfire/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_campfire iyc.data 1
scoreboard players remove #total_stone_campfire iyc.data 1

# Kill the custom block entity
kill @s

