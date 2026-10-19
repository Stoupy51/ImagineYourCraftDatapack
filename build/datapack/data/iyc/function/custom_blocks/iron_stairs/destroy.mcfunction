
#> iyc:custom_blocks/iron_stairs/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_waxed_cut_copper_stairs
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:waxed_cut_copper_stairs"}},distance=..1] run function iyc:custom_blocks/iron_stairs/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_waxed_cut_copper_stairs iyc.data 1
scoreboard players remove #total_iron_stairs iyc.data 1

# Kill the custom block entity
kill @s

