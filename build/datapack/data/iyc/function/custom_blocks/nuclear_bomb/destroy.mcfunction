
#> iyc:custom_blocks/nuclear_bomb/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_tnt
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:tnt"}},distance=..1] run function iyc:custom_blocks/nuclear_bomb/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_tnt iyc.data 1
scoreboard players remove #total_nuclear_bomb iyc.data 1

# Kill the custom block entity
kill @s

