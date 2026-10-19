
#> iyc:custom_blocks/redstone_lamp_always/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_ochre_froglight
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:ochre_froglight"}},distance=..1] run function iyc:custom_blocks/redstone_lamp_always/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_ochre_froglight iyc.data 1
scoreboard players remove #total_redstone_lamp_always iyc.data 1

# Kill the custom block entity
kill @s

