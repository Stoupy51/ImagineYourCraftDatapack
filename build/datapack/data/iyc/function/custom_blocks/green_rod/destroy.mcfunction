
#> iyc:custom_blocks/green_rod/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_structure_void
#

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_structure_void iyc.data 1
scoreboard players remove #total_green_rod iyc.data 1

# Kill the custom block entity
kill @s

# Break feedback, the item, and the interaction gone
particle minecraft:item{item:{id:"minecraft:furnace",components:{"minecraft:item_model":"iyc:green_rod"}}} ~ ~ ~ 0.25 0.25 0.25 0.1 30
playsound minecraft:block.wood.break block @a ~ ~ ~ 1.0
execute unless score #no_drop iyc.data matches 1 run loot spawn ~ ~ ~ loot iyc:i/green_rod
execute positioned ~ ~-0.5 ~ run kill @e[type=interaction,tag=iyc.interaction,distance=..0.01]

