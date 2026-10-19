
#> iyc:custom_blocks/lava_effect_generator/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_cobblestone
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:cobblestone"}},distance=..1] run function iyc:custom_blocks/lava_effect_generator/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_cobblestone iyc.data 1
scoreboard players remove #total_lava_effect_generator iyc.data 1

# Kill the custom block entity
kill @s

# Decrease the number of entities with second tag
scoreboard players remove #second_entities iyc.data 1

