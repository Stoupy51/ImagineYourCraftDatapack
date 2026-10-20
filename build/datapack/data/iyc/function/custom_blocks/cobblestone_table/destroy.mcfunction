
#> iyc:custom_blocks/cobblestone_table/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_barrier
#

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_barrier iyc.data 1
scoreboard players remove #total_cobblestone_table iyc.data 1

# Kill the custom block entity
kill @s

# Break feedback, the item, and the interaction gone
particle minecraft:item{item:{id:"minecraft:furnace",components:{"minecraft:item_model":"iyc:cobblestone_table"}}} ~ ~ ~ 0.25 0.25 0.25 0.1 30
playsound minecraft:block.stone.break block @a ~ ~ ~ 1.0
execute unless score #no_drop iyc.data matches 1 run loot spawn ~ ~ ~ loot iyc:i/cobblestone_table
execute positioned ~ ~-0.5 ~ run kill @e[type=interaction,tag=iyc.interaction,distance=..0.01]

