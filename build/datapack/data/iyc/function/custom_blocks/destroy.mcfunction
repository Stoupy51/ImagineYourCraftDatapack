
#> iyc:custom_blocks/destroy
#
# @within	iyc:v0.0.1/tick_2
#			iyc:v0.0.1/second
#			iyc:v0.0.1/second_5
#			iyc:calls/common_signals/on_ore_destroyed
#

execute if score #total_vanilla_cake iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_cake] unless block ~ ~ ~ minecraft:cake run function iyc:custom_blocks/_groups/minecraft_cake
execute if score #total_vanilla_coal_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_coal_block] unless block ~ ~ ~ minecraft:coal_block run function iyc:custom_blocks/_groups/minecraft_coal_block
execute if score #total_vanilla_diamond_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_diamond_block] unless block ~ ~ ~ minecraft:diamond_block run function iyc:custom_blocks/_groups/minecraft_diamond_block
execute if score #total_vanilla_furnace iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_furnace] unless block ~ ~ ~ minecraft:furnace run function iyc:custom_blocks/_groups/minecraft_furnace
execute if score #total_vanilla_glass iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_glass] unless block ~ ~ ~ minecraft:glass run function iyc:custom_blocks/_groups/minecraft_glass
execute if score #total_vanilla_iron_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_iron_block] unless block ~ ~ ~ minecraft:iron_block run function iyc:custom_blocks/_groups/minecraft_iron_block
execute if score #total_vanilla_ladder iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_ladder] unless block ~ ~ ~ minecraft:ladder run function iyc:custom_blocks/_groups/minecraft_ladder
execute if score #total_vanilla_netherite_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_netherite_block] unless block ~ ~ ~ minecraft:netherite_block run function iyc:custom_blocks/_groups/minecraft_netherite_block
execute if score #total_vanilla_oak_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_planks] unless block ~ ~ ~ minecraft:oak_planks run function iyc:custom_blocks/_groups/minecraft_oak_planks
execute if score #total_vanilla_ochre_froglight iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_ochre_froglight] unless block ~ ~ ~ minecraft:ochre_froglight run function iyc:custom_blocks/_groups/minecraft_ochre_froglight
execute if score #total_vanilla_polished_deepslate iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_polished_deepslate] unless block ~ ~ ~ minecraft:polished_deepslate run function iyc:custom_blocks/_groups/minecraft_polished_deepslate
execute if score #total_vanilla_red_concrete iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_red_concrete] unless block ~ ~ ~ minecraft:red_concrete run function iyc:custom_blocks/_groups/minecraft_red_concrete
execute if score #total_vanilla_structure_void iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_structure_void] unless block ~ ~ ~ minecraft:structure_void run function iyc:custom_blocks/_groups/minecraft_structure_void
execute if score #total_vanilla_tnt iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_tnt] unless block ~ ~ ~ minecraft:tnt run function iyc:custom_blocks/_groups/minecraft_tnt
execute if score #total_vanilla_torch iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_torch] unless block ~ ~ ~ minecraft:torch run function iyc:custom_blocks/_groups/minecraft_torch
execute if score #total_vanilla_wheat iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_wheat] unless block ~ ~ ~ minecraft:wheat run function iyc:custom_blocks/_groups/minecraft_wheat

