
#> iyc:v0.1.0/second
#
# @within	iyc:v0.1.0/tick
#

# Reset timer
scoreboard players set #second iyc.data 0

# Seats left empty
execute if score #seats iyc.data matches 1.. as @e[type=item_display,tag=iyc.seat] unless predicate {"type": "minecraft:entity_properties","entity": "this","predicate": {"passenger": {}}} run function iyc:custom_blocks/_interaction/unseat

# 1 second break detection (any custom block)
execute if score #total_custom_blocks iyc.data matches 1.. as @e[type=#iyc:custom_blocks,tag=iyc.custom_block,tag=!iyc.vanilla.minecraft_polished_deepslate,predicate=!iyc:advanced_check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

execute as @e[type=item_display,tag=iyc.follow] at @s run function iyc:shapes/follow

# Custom blocks second functions
execute if score #second_entities iyc.data matches 1.. as @e[tag=iyc.second] at @s run function iyc:custom_blocks/second

