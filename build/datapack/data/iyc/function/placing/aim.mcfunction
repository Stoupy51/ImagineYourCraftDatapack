
#> iyc:placing/aim
#
# @executed	at @s
#
# @within	iyc:custom_blocks/log_stairs/place_secondary
#			iyc:custom_blocks/glowstone_stairs/place_secondary
#			iyc:custom_blocks/iron_stairs/place_secondary
#			iyc:custom_blocks/obsidian_stairs/place_secondary
#			iyc:custom_blocks/step_stairs/place_secondary
#			iyc:custom_blocks/slate_stairs/place_secondary
#			iyc:custom_blocks/oak_reversed_planks_stairs/place_secondary
#			iyc:custom_blocks/glass_stairs/place_secondary
#			iyc:custom_blocks/glass_slab/place_secondary
#			iyc:custom_blocks/stone_slopes/place_secondary
#			iyc:custom_blocks/slate_slopes/place_secondary
#			iyc:custom_blocks/sandstone_slopes/place_secondary
#			iyc:custom_blocks/glowstone_slopes/place_secondary
#			iyc:custom_blocks/oak_planks_slopes/place_secondary
#			iyc:custom_blocks/spruce_planks_slopes/place_secondary
#			iyc:custom_blocks/birch_planks_slopes/place_secondary
#			iyc:custom_blocks/jungle_planks_slopes/place_secondary
#			iyc:custom_blocks/oak_log_slopes/place_secondary
#			iyc:custom_blocks/spruce_log_slopes/place_secondary
#			iyc:custom_blocks/birch_log_slopes/place_secondary
#			iyc:custom_blocks/jungle_log_slopes/place_secondary
#			iyc:custom_blocks/glass_slopes/place_secondary
#			iyc:custom_blocks/netherrack_slab/place_secondary
#			iyc:custom_blocks/reversed_planks_slab/place_secondary
#			iyc:custom_blocks/obsidian_slab/place_secondary
#			iyc:custom_blocks/oak_log_slab/place_secondary
#			iyc:custom_blocks/glowstone_slab/place_secondary
#			iyc:custom_blocks/slate_slab/place_secondary
#			iyc:custom_blocks/stone_trapdoor/place_secondary
#			iyc:custom_blocks/glowstone_trapdoor/place_secondary
#			iyc:custom_blocks/glowstone_fence_gate/place_secondary
#			iyc:custom_blocks/log_fence_gate/place_secondary
#			iyc:custom_blocks/stone_fence_gate/place_secondary
#			iyc:custom_blocks/iron_fence_gate/place_secondary
#			iyc:placing/marker_aim
#

tag @s add iyc.placing
scoreboard players set #upper iyc.data 0
scoreboard players set #floor iyc.data 0
scoreboard players set #inside iyc.data 0
scoreboard players set #steps iyc.data 0
execute as @p[tag=iyc.placer] at @s anchored eyes positioned ^ ^ ^ anchored feet run function iyc:placing/ray
tag @s remove iyc.placing

