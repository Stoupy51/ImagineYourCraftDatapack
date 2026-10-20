
#> iyc:custom_blocks/magenta_cloud/destroy
#
# @executed	at @s
#
# @within	iyc:custom_blocks/no_block_below
#			iyc:custom_blocks/_groups/minecraft_structure_void
#

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_structure_void iyc.data 1
scoreboard players remove #total_magenta_cloud iyc.data 1

# Kill the custom block entity
kill @s

# Break feedback, the item, and the interaction gone
particle minecraft:item{item:{id:"minecraft:furnace",components:{"minecraft:item_model":"iyc:magenta_cloud"}}} ~ ~ ~ 0.25 0.25 0.25 0.1 30
playsound minecraft:block.wool.break block @a ~ ~ ~ 1.0
execute unless score #no_drop iyc.data matches 1 run loot spawn ~ ~ ~ loot iyc:i/magenta_cloud
execute positioned ~ ~-0.5 ~ run kill @e[type=interaction,tag=iyc.interaction,distance=..0.01]

