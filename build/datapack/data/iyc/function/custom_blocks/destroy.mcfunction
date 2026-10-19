
#> iyc:custom_blocks/destroy
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:v0.1.0/tick_2 [ as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s ]
#			iyc:v0.1.0/second [ as @e[type=#iyc:custom_blocks,tag=...,predicate=!iyc:advanced_check_vanilla_blocks] & at @s ]
#			iyc:v0.1.0/second_5 [ as @e[type=item_display,tag=iyc.custom_block,predicate=!iyc:advanced_check_vanilla_blocks] & at @s ]
#			iyc:calls/common_signals/custom_block_destroy [ as @e[tag=iyc.custom_block,dx=0,dy=0,dz=0] & at @s ]
#			iyc:interaction/break [ as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] ]
#			iyc:interaction/light [ as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] ]
#

# Check for missing vanilla blocks
execute if score #total_vanilla_acacia_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_acacia_planks] unless block ~ ~ ~ minecraft:acacia_planks run return run function iyc:custom_blocks/_groups/minecraft_acacia_planks
execute if score #total_vanilla_barrel iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_barrel] unless block ~ ~ ~ minecraft:barrel run return run function iyc:custom_blocks/_groups/minecraft_barrel
execute if score #total_vanilla_barrier iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_barrier] unless block ~ ~ ~ minecraft:barrier run return run function iyc:custom_blocks/_groups/minecraft_barrier
execute if score #total_vanilla_birch_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_birch_planks] unless block ~ ~ ~ minecraft:birch_planks run return run function iyc:custom_blocks/_groups/minecraft_birch_planks
execute if score #total_vanilla_brewing_stand iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_brewing_stand] unless block ~ ~ ~ minecraft:brewing_stand run return run function iyc:custom_blocks/_groups/minecraft_brewing_stand
execute if score #total_vanilla_cake iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_cake] unless block ~ ~ ~ minecraft:cake run return run function iyc:custom_blocks/_groups/minecraft_cake
execute if score #total_vanilla_campfire iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_campfire] unless block ~ ~ ~ minecraft:campfire run return run function iyc:custom_blocks/_groups/minecraft_campfire
execute if score #total_vanilla_cherry_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_cherry_planks] unless block ~ ~ ~ minecraft:cherry_planks run return run function iyc:custom_blocks/_groups/minecraft_cherry_planks
execute if score #total_vanilla_coal_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_coal_block] unless block ~ ~ ~ minecraft:coal_block run return run function iyc:custom_blocks/_groups/minecraft_coal_block
execute if score #total_vanilla_cobblestone iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_cobblestone] unless block ~ ~ ~ minecraft:cobblestone run return run function iyc:custom_blocks/_groups/minecraft_cobblestone
execute if score #total_vanilla_cobblestone_wall iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_cobblestone_wall] unless block ~ ~ ~ minecraft:cobblestone_wall run return run function iyc:custom_blocks/_groups/minecraft_cobblestone_wall
execute if score #total_vanilla_dark_oak_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_dark_oak_planks] unless block ~ ~ ~ minecraft:dark_oak_planks run return run function iyc:custom_blocks/_groups/minecraft_dark_oak_planks
execute if score #total_vanilla_diamond_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_diamond_block] unless block ~ ~ ~ minecraft:diamond_block run return run function iyc:custom_blocks/_groups/minecraft_diamond_block
execute if score #total_vanilla_furnace iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_furnace] unless block ~ ~ ~ minecraft:furnace run return run function iyc:custom_blocks/_groups/minecraft_furnace
execute if score #total_vanilla_glass iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_glass] unless block ~ ~ ~ minecraft:glass run return run function iyc:custom_blocks/_groups/minecraft_glass
execute if score #total_vanilla_iron_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_iron_block] unless block ~ ~ ~ minecraft:iron_block run return run function iyc:custom_blocks/_groups/minecraft_iron_block
execute if score #total_vanilla_jungle_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_jungle_planks] unless block ~ ~ ~ minecraft:jungle_planks run return run function iyc:custom_blocks/_groups/minecraft_jungle_planks
execute if score #total_vanilla_ladder iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_ladder] unless block ~ ~ ~ minecraft:ladder run return run function iyc:custom_blocks/_groups/minecraft_ladder
execute if score #total_vanilla_light iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_light] unless block ~ ~ ~ minecraft:light run return run function iyc:custom_blocks/_groups/minecraft_light
execute if score #total_vanilla_nether_brick_fence iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_nether_brick_fence] unless block ~ ~ ~ minecraft:nether_brick_fence run return run function iyc:custom_blocks/_groups/minecraft_nether_brick_fence
execute if score #total_vanilla_nether_brick_slab iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_nether_brick_slab] unless block ~ ~ ~ minecraft:nether_brick_slab run return run function iyc:custom_blocks/_groups/minecraft_nether_brick_slab
execute if score #total_vanilla_netherite_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_netherite_block] unless block ~ ~ ~ minecraft:netherite_block run return run function iyc:custom_blocks/_groups/minecraft_netherite_block
execute if score #total_vanilla_oak_fence iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_fence] unless block ~ ~ ~ minecraft:oak_fence run return run function iyc:custom_blocks/_groups/minecraft_oak_fence
execute if score #total_vanilla_oak_fence_gate iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_fence_gate] unless block ~ ~ ~ minecraft:oak_fence_gate run return run function iyc:custom_blocks/_groups/minecraft_oak_fence_gate
execute if score #total_vanilla_oak_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_planks] unless block ~ ~ ~ minecraft:oak_planks run return run function iyc:custom_blocks/_groups/minecraft_oak_planks
execute if score #total_vanilla_oak_slab iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_slab] unless block ~ ~ ~ minecraft:oak_slab run return run function iyc:custom_blocks/_groups/minecraft_oak_slab
execute if score #total_vanilla_oak_stairs iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_stairs] unless block ~ ~ ~ minecraft:oak_stairs run return run function iyc:custom_blocks/_groups/minecraft_oak_stairs
execute if score #total_vanilla_oak_trapdoor iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_oak_trapdoor] unless block ~ ~ ~ minecraft:oak_trapdoor run return run function iyc:custom_blocks/_groups/minecraft_oak_trapdoor
execute if score #total_vanilla_ochre_froglight iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_ochre_froglight] unless block ~ ~ ~ minecraft:ochre_froglight run return run function iyc:custom_blocks/_groups/minecraft_ochre_froglight
execute if score #total_vanilla_polished_deepslate iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_polished_deepslate] unless block ~ ~ ~ minecraft:polished_deepslate run return run function iyc:custom_blocks/_groups/minecraft_polished_deepslate
execute if score #total_vanilla_raw_iron_block iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_raw_iron_block] unless block ~ ~ ~ minecraft:raw_iron_block run return run function iyc:custom_blocks/_groups/minecraft_raw_iron_block
execute if score #total_vanilla_redstone_lamp iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_redstone_lamp] unless block ~ ~ ~ minecraft:redstone_lamp run return run function iyc:custom_blocks/_groups/minecraft_redstone_lamp
execute if score #total_vanilla_smooth_stone iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_smooth_stone] unless block ~ ~ ~ minecraft:smooth_stone run return run function iyc:custom_blocks/_groups/minecraft_smooth_stone
execute if score #total_vanilla_spruce_planks iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_spruce_planks] unless block ~ ~ ~ minecraft:spruce_planks run return run function iyc:custom_blocks/_groups/minecraft_spruce_planks
execute if score #total_vanilla_stone_pressure_plate iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_stone_pressure_plate] unless block ~ ~ ~ minecraft:stone_pressure_plate run return run function iyc:custom_blocks/_groups/minecraft_stone_pressure_plate
execute if score #total_vanilla_stone_slab iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_stone_slab] unless block ~ ~ ~ minecraft:stone_slab run return run function iyc:custom_blocks/_groups/minecraft_stone_slab
execute if score #total_vanilla_stone_stairs iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_stone_stairs] unless block ~ ~ ~ minecraft:stone_stairs run return run function iyc:custom_blocks/_groups/minecraft_stone_stairs
execute if score #total_vanilla_structure_void iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_structure_void] unless block ~ ~ ~ minecraft:structure_void run return run function iyc:custom_blocks/_groups/minecraft_structure_void
execute if score #total_vanilla_tnt iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_tnt] unless block ~ ~ ~ minecraft:tnt run return run function iyc:custom_blocks/_groups/minecraft_tnt
execute if score #total_vanilla_torch iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_torch] unless block ~ ~ ~ minecraft:torch run return run function iyc:custom_blocks/_groups/minecraft_torch
execute if score #total_vanilla_tripwire iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_tripwire] unless block ~ ~ ~ minecraft:tripwire run return run function iyc:custom_blocks/_groups/minecraft_tripwire
execute if score #total_vanilla_wall_torch iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_wall_torch] unless block ~ ~ ~ minecraft:wall_torch run return run function iyc:custom_blocks/_groups/minecraft_wall_torch
execute if score #total_vanilla_waxed_cut_copper_stairs iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_waxed_cut_copper_stairs] unless block ~ ~ ~ minecraft:waxed_cut_copper_stairs run return run function iyc:custom_blocks/_groups/minecraft_waxed_cut_copper_stairs
execute if score #total_vanilla_wheat iyc.data matches 1.. if entity @s[tag=iyc.vanilla.minecraft_wheat] unless block ~ ~ ~ minecraft:wheat run return run function iyc:custom_blocks/_groups/minecraft_wheat

