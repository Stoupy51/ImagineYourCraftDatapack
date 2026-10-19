
#> iyc:custom_blocks/red_lit_lamp/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_light
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:light"}},distance=..1] run function iyc:custom_blocks/red_lit_lamp/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_light iyc.data 1
scoreboard players remove #total_red_lit_lamp iyc.data 1

# Kill the custom block entity
kill @s

execute if score #break_drop iyc.data matches 1 run loot spawn ~ ~ ~ loot iyc:i/red_lamp
kill @e[type=interaction,tag=iyc.interaction,distance=..0.6]

