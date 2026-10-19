
#> iyc:custom_blocks/iron_furnace/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_furnace
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:furnace"}},distance=..1] run function iyc:custom_blocks/iron_furnace/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_furnace iyc.data 1
scoreboard players remove #total_iron_furnace iyc.data 1

# Kill the custom block entity
kill @s

# Decrease the number of entities with tick tag
scoreboard players remove #tick_entities iyc.data 1

