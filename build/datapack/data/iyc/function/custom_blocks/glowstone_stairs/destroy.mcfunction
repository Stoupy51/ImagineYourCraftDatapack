
#> iyc:custom_blocks/glowstone_stairs/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_oak_stairs
#

function iyc:glow/clear

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:oak_stairs"}},distance=..1] run function iyc:custom_blocks/glowstone_stairs/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_oak_stairs iyc.data 1
scoreboard players remove #total_glowstone_stairs iyc.data 1

# Kill the custom block entity
kill @s

# Decrease the number of entities with second tag
scoreboard players remove #second_entities iyc.data 1

