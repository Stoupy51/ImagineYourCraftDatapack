
#> iyc:custom_blocks/_groups/minecraft_barrier
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_glass_stairs iyc.data matches 1.. if entity @s[tag=iyc.glass_stairs] run function iyc:custom_blocks/glass_stairs/destroy
execute if score #total_glass_slab iyc.data matches 1.. if entity @s[tag=iyc.glass_slab] run function iyc:custom_blocks/glass_slab/destroy
execute if score #total_stone_slopes iyc.data matches 1.. if entity @s[tag=iyc.stone_slopes] run function iyc:custom_blocks/stone_slopes/destroy
execute if score #total_slate_slopes iyc.data matches 1.. if entity @s[tag=iyc.slate_slopes] run function iyc:custom_blocks/slate_slopes/destroy
execute if score #total_sandstone_slopes iyc.data matches 1.. if entity @s[tag=iyc.sandstone_slopes] run function iyc:custom_blocks/sandstone_slopes/destroy
execute if score #total_glowstone_slopes iyc.data matches 1.. if entity @s[tag=iyc.glowstone_slopes] run function iyc:custom_blocks/glowstone_slopes/destroy
execute if score #total_oak_planks_slopes iyc.data matches 1.. if entity @s[tag=iyc.oak_planks_slopes] run function iyc:custom_blocks/oak_planks_slopes/destroy
execute if score #total_spruce_planks_slopes iyc.data matches 1.. if entity @s[tag=iyc.spruce_planks_slopes] run function iyc:custom_blocks/spruce_planks_slopes/destroy
execute if score #total_birch_planks_slopes iyc.data matches 1.. if entity @s[tag=iyc.birch_planks_slopes] run function iyc:custom_blocks/birch_planks_slopes/destroy
execute if score #total_jungle_planks_slopes iyc.data matches 1.. if entity @s[tag=iyc.jungle_planks_slopes] run function iyc:custom_blocks/jungle_planks_slopes/destroy
execute if score #total_oak_log_slopes iyc.data matches 1.. if entity @s[tag=iyc.oak_log_slopes] run function iyc:custom_blocks/oak_log_slopes/destroy
execute if score #total_spruce_log_slopes iyc.data matches 1.. if entity @s[tag=iyc.spruce_log_slopes] run function iyc:custom_blocks/spruce_log_slopes/destroy
execute if score #total_birch_log_slopes iyc.data matches 1.. if entity @s[tag=iyc.birch_log_slopes] run function iyc:custom_blocks/birch_log_slopes/destroy
execute if score #total_jungle_log_slopes iyc.data matches 1.. if entity @s[tag=iyc.jungle_log_slopes] run function iyc:custom_blocks/jungle_log_slopes/destroy
execute if score #total_glass_slopes iyc.data matches 1.. if entity @s[tag=iyc.glass_slopes] run function iyc:custom_blocks/glass_slopes/destroy
execute if score #total_oak_table iyc.data matches 1.. if entity @s[tag=iyc.oak_table] run function iyc:custom_blocks/oak_table/destroy
execute if score #total_birch_table iyc.data matches 1.. if entity @s[tag=iyc.birch_table] run function iyc:custom_blocks/birch_table/destroy
execute if score #total_cobblestone_table iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_table] run function iyc:custom_blocks/cobblestone_table/destroy
execute if score #total_stone_table iyc.data matches 1.. if entity @s[tag=iyc.stone_table] run function iyc:custom_blocks/stone_table/destroy
execute if score #total_oak_little_table iyc.data matches 1.. if entity @s[tag=iyc.oak_little_table] run function iyc:custom_blocks/oak_little_table/destroy
execute if score #total_birch_little_table iyc.data matches 1.. if entity @s[tag=iyc.birch_little_table] run function iyc:custom_blocks/birch_little_table/destroy
execute if score #total_cobblestone_little_table iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_little_table] run function iyc:custom_blocks/cobblestone_little_table/destroy
execute if score #total_stone_little_table iyc.data matches 1.. if entity @s[tag=iyc.stone_little_table] run function iyc:custom_blocks/stone_little_table/destroy
execute if score #total_oak_stool iyc.data matches 1.. if entity @s[tag=iyc.oak_stool] run function iyc:custom_blocks/oak_stool/destroy
execute if score #total_birch_stool iyc.data matches 1.. if entity @s[tag=iyc.birch_stool] run function iyc:custom_blocks/birch_stool/destroy
execute if score #total_cobblestone_stool iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_stool] run function iyc:custom_blocks/cobblestone_stool/destroy
execute if score #total_stone_stool iyc.data matches 1.. if entity @s[tag=iyc.stone_stool] run function iyc:custom_blocks/stone_stool/destroy
execute if score #total_oak_high_stool iyc.data matches 1.. if entity @s[tag=iyc.oak_high_stool] run function iyc:custom_blocks/oak_high_stool/destroy
execute if score #total_birch_high_stool iyc.data matches 1.. if entity @s[tag=iyc.birch_high_stool] run function iyc:custom_blocks/birch_high_stool/destroy
execute if score #total_cobblestone_high_stool iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_high_stool] run function iyc:custom_blocks/cobblestone_high_stool/destroy
execute if score #total_stone_high_stool iyc.data matches 1.. if entity @s[tag=iyc.stone_high_stool] run function iyc:custom_blocks/stone_high_stool/destroy
execute if score #total_oak_bench iyc.data matches 1.. if entity @s[tag=iyc.oak_bench] run function iyc:custom_blocks/oak_bench/destroy
execute if score #total_birch_bench iyc.data matches 1.. if entity @s[tag=iyc.birch_bench] run function iyc:custom_blocks/birch_bench/destroy
execute if score #total_cobblestone_bench iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_bench] run function iyc:custom_blocks/cobblestone_bench/destroy
execute if score #total_stone_bench iyc.data matches 1.. if entity @s[tag=iyc.stone_bench] run function iyc:custom_blocks/stone_bench/destroy
execute if score #total_oak_chair iyc.data matches 1.. if entity @s[tag=iyc.oak_chair] run function iyc:custom_blocks/oak_chair/destroy
execute if score #total_birch_chair iyc.data matches 1.. if entity @s[tag=iyc.birch_chair] run function iyc:custom_blocks/birch_chair/destroy
execute if score #total_cobblestone_chair iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_chair] run function iyc:custom_blocks/cobblestone_chair/destroy
execute if score #total_stone_chair iyc.data matches 1.. if entity @s[tag=iyc.stone_chair] run function iyc:custom_blocks/stone_chair/destroy
execute if score #total_oak_shelf iyc.data matches 1.. if entity @s[tag=iyc.oak_shelf] run function iyc:custom_blocks/oak_shelf/destroy
execute if score #total_white_blob iyc.data matches 1.. if entity @s[tag=iyc.white_blob] run function iyc:custom_blocks/white_blob/destroy
execute if score #total_orange_blob iyc.data matches 1.. if entity @s[tag=iyc.orange_blob] run function iyc:custom_blocks/orange_blob/destroy
execute if score #total_magenta_blob iyc.data matches 1.. if entity @s[tag=iyc.magenta_blob] run function iyc:custom_blocks/magenta_blob/destroy
execute if score #total_light_blue_blob iyc.data matches 1.. if entity @s[tag=iyc.light_blue_blob] run function iyc:custom_blocks/light_blue_blob/destroy
execute if score #total_yellow_blob iyc.data matches 1.. if entity @s[tag=iyc.yellow_blob] run function iyc:custom_blocks/yellow_blob/destroy
execute if score #total_lime_blob iyc.data matches 1.. if entity @s[tag=iyc.lime_blob] run function iyc:custom_blocks/lime_blob/destroy
execute if score #total_pink_blob iyc.data matches 1.. if entity @s[tag=iyc.pink_blob] run function iyc:custom_blocks/pink_blob/destroy
execute if score #total_gray_blob iyc.data matches 1.. if entity @s[tag=iyc.gray_blob] run function iyc:custom_blocks/gray_blob/destroy
execute if score #total_light_gray_blob iyc.data matches 1.. if entity @s[tag=iyc.light_gray_blob] run function iyc:custom_blocks/light_gray_blob/destroy
execute if score #total_cyan_blob iyc.data matches 1.. if entity @s[tag=iyc.cyan_blob] run function iyc:custom_blocks/cyan_blob/destroy
execute if score #total_purple_blob iyc.data matches 1.. if entity @s[tag=iyc.purple_blob] run function iyc:custom_blocks/purple_blob/destroy
execute if score #total_blue_blob iyc.data matches 1.. if entity @s[tag=iyc.blue_blob] run function iyc:custom_blocks/blue_blob/destroy
execute if score #total_brown_blob iyc.data matches 1.. if entity @s[tag=iyc.brown_blob] run function iyc:custom_blocks/brown_blob/destroy
execute if score #total_green_blob iyc.data matches 1.. if entity @s[tag=iyc.green_blob] run function iyc:custom_blocks/green_blob/destroy
execute if score #total_red_blob iyc.data matches 1.. if entity @s[tag=iyc.red_blob] run function iyc:custom_blocks/red_blob/destroy
execute if score #total_black_blob iyc.data matches 1.. if entity @s[tag=iyc.black_blob] run function iyc:custom_blocks/black_blob/destroy

