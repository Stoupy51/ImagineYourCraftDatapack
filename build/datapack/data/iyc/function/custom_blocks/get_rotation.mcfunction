
#> iyc:custom_blocks/get_rotation
#
# @within	iyc:custom_blocks/log_stairs/place_main
#			iyc:custom_blocks/glowstone_stairs/place_main
#			iyc:custom_blocks/iron_stairs/place_main
#			iyc:custom_blocks/obsidian_stairs/place_main
#			iyc:custom_blocks/step_stairs/place_main
#			iyc:custom_blocks/slate_stairs/place_main
#			iyc:custom_blocks/oak_reversed_planks_stairs/place_main
#			iyc:custom_blocks/glass_stairs/place_main
#			iyc:custom_blocks/glass_slab/place_main
#			iyc:custom_blocks/stone_slopes/place_main
#			iyc:custom_blocks/slate_slopes/place_main
#			iyc:custom_blocks/sandstone_slopes/place_main
#			iyc:custom_blocks/glowstone_slopes/place_main
#			iyc:custom_blocks/oak_planks_slopes/place_main
#			iyc:custom_blocks/spruce_planks_slopes/place_main
#			iyc:custom_blocks/birch_planks_slopes/place_main
#			iyc:custom_blocks/jungle_planks_slopes/place_main
#			iyc:custom_blocks/oak_log_slopes/place_main
#			iyc:custom_blocks/spruce_log_slopes/place_main
#			iyc:custom_blocks/birch_log_slopes/place_main
#			iyc:custom_blocks/jungle_log_slopes/place_main
#			iyc:custom_blocks/glass_slopes/place_main
#			iyc:custom_blocks/stone_trapdoor/place_main
#			iyc:custom_blocks/glowstone_trapdoor/place_main
#			iyc:custom_blocks/iron_ladder/place_main
#			iyc:custom_blocks/glowstone_fence_gate/place_main
#			iyc:custom_blocks/log_fence_gate/place_main
#			iyc:custom_blocks/stone_fence_gate/place_main
#			iyc:custom_blocks/iron_fence_gate/place_main
#			iyc:custom_blocks/lignite_wall_torch/place_main
#			iyc:custom_blocks/oak_chair/place_main
#			iyc:custom_blocks/birch_chair/place_main
#			iyc:custom_blocks/cobblestone_chair/place_main
#			iyc:custom_blocks/stone_chair/place_main
#			iyc:custom_blocks/oak_shelf/place_main
#			iyc:custom_blocks/iron_furnace/place_main
#

# Set up score
scoreboard players set #rotation iyc.data 0

# Player case
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=-46..45] run scoreboard players set #rotation iyc.data 1
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=45..135] run scoreboard players set #rotation iyc.data 2
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=135..225] run scoreboard players set #rotation iyc.data 3
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=225..315] run scoreboard players set #rotation iyc.data 4

# Predicate case
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/north run scoreboard players set #rotation iyc.data 1
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/east run scoreboard players set #rotation iyc.data 2
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/south run scoreboard players set #rotation iyc.data 3
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/west run scoreboard players set #rotation iyc.data 4
# No more cases for now

