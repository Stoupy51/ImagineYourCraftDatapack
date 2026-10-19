
#> iyc:custom_blocks/steel_brewing_stand/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_brewing_stand
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:brewing_stand"}},distance=..1] run function iyc:custom_blocks/steel_brewing_stand/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_brewing_stand iyc.data 1
scoreboard players remove #total_steel_brewing_stand iyc.data 1

# Kill the custom block entity
kill @s

# Decrease the number of entities with tick tag
scoreboard players remove #tick_entities iyc.data 1

