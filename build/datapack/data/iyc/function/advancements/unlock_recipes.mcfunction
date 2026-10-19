
#> iyc:advancements/unlock_recipes
#
# @executed	as the player & at current position
#
# @within	advancement iyc:unlock_recipes
#

# Revoke advancement
advancement revoke @s only iyc:unlock_recipes

## For each ingredient in inventory, unlock the recipes
# minecraft:emerald
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:emerald
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_axe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_boots
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_chestplate
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_helmet
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_hoe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_leggings
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_pickaxe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_shovel
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_sword

# minecraft:stick
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:stick
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_axe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_hoe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_pickaxe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_shovel
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_sword
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:log_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_plank_wall
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:white_iron_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:white_rod

# minecraft:obsidian
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:obsidian
execute if score #success iyc.data matches 1 run recipe give @s iyc:obsidian_ingot
execute if score #success iyc.data matches 1 run recipe give @s iyc:obsidian_ingot_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:obsidian_slab

# minecraft:stone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:stone
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_stick
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_wall

# minecraft:glass
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:beer_mug
execute if score #success iyc.data matches 1 run recipe give @s iyc:blue_block_ctf
execute if score #success iyc.data matches 1 run recipe give @s iyc:clear_glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:empty_glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:flatware
execute if score #success iyc.data matches 1 run recipe give @s iyc:glass_slab
execute if score #success iyc.data matches 1 run recipe give @s iyc:glass_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:glass_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:glass_stairs
execute if score #success iyc.data matches 1 run recipe give @s iyc:hot_chocolate
execute if score #success iyc.data matches 1 run recipe give @s iyc:nutella
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_block_ctf
execute if score #success iyc.data matches 1 run recipe give @s iyc:transparent_light_block

# minecraft:iron_ingot
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:iron_ingot
execute if score #success iyc.data matches 1 run recipe give @s iyc:can
execute if score #success iyc.data matches 1 run recipe give @s iyc:chainmail
execute if score #success iyc.data matches 1 run recipe give @s iyc:flatware
execute if score #success iyc.data matches 1 run recipe give @s iyc:helice_hat
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_furnace
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_ladder
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_stairs
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_barrel
execute if score #success iyc.data matches 1 run recipe give @s iyc:white_iron_fence

# minecraft:cocoa_beans
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:cocoa_beans
execute if score #success iyc.data matches 1 run recipe give @s iyc:hot_chocolate
execute if score #success iyc.data matches 1 run recipe give @s iyc:nutella

# minecraft:bread
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:bread
execute if score #success iyc.data matches 1 run recipe give @s iyc:toast

# minecraft:elytra
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:elytra
execute if score #success iyc.data matches 1 run recipe give @s iyc:helice_hat

# minecraft:oak_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:oak_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:log_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:log_stairs
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_log_slab
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_log_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_log_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_log_wall
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_oak_planks

# minecraft:spruce_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:spruce_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_spruce_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_log_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_log_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_wood_lantern

# minecraft:birch_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:birch_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_log_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_log_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_birch_planks

# minecraft:jungle_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:jungle_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_log_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_log_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_jungle_planks

# minecraft:acacia_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:acacia_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_acacia_planks

# minecraft:dark_oak_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:dark_oak_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_dark_oak_planks

# minecraft:cherry_log
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:cherry_log
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_cherry_planks

# minecraft:smooth_stone_slab
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:smooth_stone_slab
execute if score #success iyc.data matches 1 run recipe give @s iyc:step_block
execute if score #success iyc.data matches 1 run recipe give @s iyc:step_stairs

# minecraft:glowstone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:glowstone
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_fence
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_pressure_plate
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_slab
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_stairs
execute if score #success iyc.data matches 1 run recipe give @s iyc:glowstone_wall
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:transparent_light_block

# minecraft:sandstone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:sandstone
execute if score #success iyc.data matches 1 run recipe give @s iyc:sandstone_campfire
execute if score #success iyc.data matches 1 run recipe give @s iyc:sandstone_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:sandstone_slopes_2

# minecraft:oak_planks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:oak_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_barrel
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_planks_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_planks_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_shelf
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_table

# minecraft:spruce_planks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:spruce_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_planks_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_planks_slopes_2

# minecraft:birch_planks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:birch_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_planks_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_planks_slopes_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_table

# minecraft:jungle_planks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:jungle_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_planks_slopes
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_planks_slopes_2

# minecraft:netherrack
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:netherrack
execute if score #success iyc.data matches 1 run recipe give @s iyc:netherrack_slab

# minecraft:redstone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:redstone
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_light

# minecraft:redstone_lamp
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:redstone_lamp
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_light

# minecraft:cobblestone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:cobblestone
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_bench
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_campfire
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_chair
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_high_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_little_table
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_stool
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_table

# minecraft:tnt
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:tnt
execute if score #success iyc.data matches 1 run recipe give @s iyc:nuclear_bomb

# minecraft:flint_and_steel
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:flint_and_steel
execute if score #success iyc.data matches 1 run recipe give @s iyc:brick_campfire
execute if score #success iyc.data matches 1 run recipe give @s iyc:cobblestone_campfire
execute if score #success iyc.data matches 1 run recipe give @s iyc:sandstone_campfire
execute if score #success iyc.data matches 1 run recipe give @s iyc:stonebrick_campfire

# minecraft:bricks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:bricks
execute if score #success iyc.data matches 1 run recipe give @s iyc:brick_campfire

# minecraft:stone_bricks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:stone_bricks
execute if score #success iyc.data matches 1 run recipe give @s iyc:stonebrick_campfire

# minecraft:white_wool
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:white_wool
execute if score #success iyc.data matches 1 run recipe give @s iyc:white_cloud

# minecraft:water_bucket
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:water_bucket
execute if score #success iyc.data matches 1 run recipe give @s iyc:white_cloud

# minecraft:blue_wool
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:blue_wool
execute if score #success iyc.data matches 1 run recipe give @s iyc:blue_block_ctf

# minecraft:red_wool
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:red_wool
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_block_ctf

# minecraft:furnace
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:furnace
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_furnace

## Add result items
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_helmet":true} }] run recipe give @s iyc:emerald_helmet
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_chestplate":true} }] run recipe give @s iyc:emerald_chestplate
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_leggings":true} }] run recipe give @s iyc:emerald_leggings
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_boots":true} }] run recipe give @s iyc:emerald_boots
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_sword":true} }] run recipe give @s iyc:emerald_sword
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_pickaxe":true} }] run recipe give @s iyc:emerald_pickaxe
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_axe":true} }] run recipe give @s iyc:emerald_axe
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_shovel":true} }] run recipe give @s iyc:emerald_shovel
execute if items entity @s container.* *[custom_data~{"iyc": {"emerald_hoe":true} }] run recipe give @s iyc:emerald_hoe
execute if items entity @s container.* *[custom_data~{"iyc": {"obsidian_ingot":true} }] run recipe give @s iyc:obsidian_ingot
execute if items entity @s container.* *[custom_data~{"iyc": {"obsidian_ingot":true} }] run recipe give @s iyc:obsidian_ingot_2
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_stick":true} }] run recipe give @s iyc:stone_stick
execute if items entity @s container.* *[custom_data~{"iyc": {"beer_mug":true} }] run recipe give @s iyc:beer_mug
execute if items entity @s container.* *[custom_data~{"iyc": {"can":true} }] run recipe give @s iyc:can
execute if items entity @s container.* *[custom_data~{"iyc": {"empty_glass":true} }] run recipe give @s iyc:empty_glass
execute if items entity @s container.* *[custom_data~{"iyc": {"hot_chocolate":true} }] run recipe give @s iyc:hot_chocolate
execute if items entity @s container.* *[custom_data~{"iyc": {"toast":true} }] run recipe give @s iyc:toast
execute if items entity @s container.* *[custom_data~{"iyc": {"nutella":true} }] run recipe give @s iyc:nutella
execute if items entity @s container.* *[custom_data~{"iyc": {"helice_hat":true} }] run recipe give @s iyc:helice_hat
execute if items entity @s container.* *[custom_data~{"iyc": {"chainmail":true} }] run recipe give @s iyc:chainmail
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_oak_planks":true} }] run recipe give @s iyc:reversed_oak_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_spruce_planks":true} }] run recipe give @s iyc:reversed_spruce_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_birch_planks":true} }] run recipe give @s iyc:reversed_birch_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_jungle_planks":true} }] run recipe give @s iyc:reversed_jungle_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_acacia_planks":true} }] run recipe give @s iyc:reversed_acacia_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_dark_oak_planks":true} }] run recipe give @s iyc:reversed_dark_oak_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"reversed_cherry_planks":true} }] run recipe give @s iyc:reversed_cherry_planks
execute if items entity @s container.* *[custom_data~{"iyc": {"step_block":true} }] run recipe give @s iyc:step_block
execute if items entity @s container.* *[custom_data~{"iyc": {"clear_glass":true} }] run recipe give @s iyc:clear_glass
execute if items entity @s container.* *[custom_data~{"iyc": {"log_stairs":true} }] run recipe give @s iyc:log_stairs
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_stairs":true} }] run recipe give @s iyc:glowstone_stairs
execute if items entity @s container.* *[custom_data~{"iyc": {"iron_stairs":true} }] run recipe give @s iyc:iron_stairs
execute if items entity @s container.* *[custom_data~{"iyc": {"step_stairs":true} }] run recipe give @s iyc:step_stairs
execute if items entity @s container.* *[custom_data~{"iyc": {"glass_stairs":true} }] run recipe give @s iyc:glass_stairs
execute if items entity @s container.* *[custom_data~{"iyc": {"glass_slab":true} }] run recipe give @s iyc:glass_slab
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_slopes":true} }] run recipe give @s iyc:stone_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_slopes":true} }] run recipe give @s iyc:stone_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"sandstone_slopes":true} }] run recipe give @s iyc:sandstone_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"sandstone_slopes":true} }] run recipe give @s iyc:sandstone_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_slopes":true} }] run recipe give @s iyc:glowstone_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_slopes":true} }] run recipe give @s iyc:glowstone_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_planks_slopes":true} }] run recipe give @s iyc:oak_planks_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_planks_slopes":true} }] run recipe give @s iyc:oak_planks_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"spruce_planks_slopes":true} }] run recipe give @s iyc:spruce_planks_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"spruce_planks_slopes":true} }] run recipe give @s iyc:spruce_planks_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_planks_slopes":true} }] run recipe give @s iyc:birch_planks_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_planks_slopes":true} }] run recipe give @s iyc:birch_planks_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"jungle_planks_slopes":true} }] run recipe give @s iyc:jungle_planks_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"jungle_planks_slopes":true} }] run recipe give @s iyc:jungle_planks_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_log_slopes":true} }] run recipe give @s iyc:oak_log_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_log_slopes":true} }] run recipe give @s iyc:oak_log_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"spruce_log_slopes":true} }] run recipe give @s iyc:spruce_log_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"spruce_log_slopes":true} }] run recipe give @s iyc:spruce_log_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_log_slopes":true} }] run recipe give @s iyc:birch_log_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_log_slopes":true} }] run recipe give @s iyc:birch_log_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"jungle_log_slopes":true} }] run recipe give @s iyc:jungle_log_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"jungle_log_slopes":true} }] run recipe give @s iyc:jungle_log_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"glass_slopes":true} }] run recipe give @s iyc:glass_slopes
execute if items entity @s container.* *[custom_data~{"iyc": {"glass_slopes":true} }] run recipe give @s iyc:glass_slopes_2
execute if items entity @s container.* *[custom_data~{"iyc": {"netherrack_slab":true} }] run recipe give @s iyc:netherrack_slab
execute if items entity @s container.* *[custom_data~{"iyc": {"obsidian_slab":true} }] run recipe give @s iyc:obsidian_slab
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_log_slab":true} }] run recipe give @s iyc:oak_log_slab
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_slab":true} }] run recipe give @s iyc:glowstone_slab
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_pressure_plate":true} }] run recipe give @s iyc:glowstone_pressure_plate
execute if items entity @s container.* *[custom_data~{"iyc": {"iron_ladder":true} }] run recipe give @s iyc:iron_ladder
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_log_wall":true} }] run recipe give @s iyc:oak_log_wall
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_wall":true} }] run recipe give @s iyc:stone_wall
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_plank_wall":true} }] run recipe give @s iyc:oak_plank_wall
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_wall":true} }] run recipe give @s iyc:glowstone_wall
execute if items entity @s container.* *[custom_data~{"iyc": {"glowstone_fence":true} }] run recipe give @s iyc:glowstone_fence
execute if items entity @s container.* *[custom_data~{"iyc": {"log_fence":true} }] run recipe give @s iyc:log_fence
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_fence":true} }] run recipe give @s iyc:stone_fence
execute if items entity @s container.* *[custom_data~{"iyc": {"white_iron_fence":true} }] run recipe give @s iyc:white_iron_fence
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_wood_lantern":true} }] run recipe give @s iyc:oak_wood_lantern
execute if items entity @s container.* *[custom_data~{"iyc": {"spruce_wood_lantern":true} }] run recipe give @s iyc:spruce_wood_lantern
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_wood_lantern":true} }] run recipe give @s iyc:birch_wood_lantern
execute if items entity @s container.* *[custom_data~{"iyc": {"jungle_wood_lantern":true} }] run recipe give @s iyc:jungle_wood_lantern
execute if items entity @s container.* *[custom_data~{"iyc": {"iron_lantern":true} }] run recipe give @s iyc:iron_lantern
execute if items entity @s container.* *[custom_data~{"iyc": {"red_light":true} }] run recipe give @s iyc:red_light
execute if items entity @s container.* *[custom_data~{"iyc": {"transparent_light_block":true} }] run recipe give @s iyc:transparent_light_block
execute if items entity @s container.* *[custom_data~{"iyc": {"white_rod":true} }] run recipe give @s iyc:white_rod
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_table":true} }] run recipe give @s iyc:oak_table
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_table":true} }] run recipe give @s iyc:birch_table
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_table":true} }] run recipe give @s iyc:cobblestone_table
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_table":true} }] run recipe give @s iyc:stone_table
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_little_table":true} }] run recipe give @s iyc:oak_little_table
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_little_table":true} }] run recipe give @s iyc:birch_little_table
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_little_table":true} }] run recipe give @s iyc:cobblestone_little_table
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_little_table":true} }] run recipe give @s iyc:stone_little_table
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_stool":true} }] run recipe give @s iyc:oak_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_stool":true} }] run recipe give @s iyc:birch_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_stool":true} }] run recipe give @s iyc:cobblestone_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_stool":true} }] run recipe give @s iyc:stone_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_high_stool":true} }] run recipe give @s iyc:oak_high_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_high_stool":true} }] run recipe give @s iyc:birch_high_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_high_stool":true} }] run recipe give @s iyc:cobblestone_high_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_high_stool":true} }] run recipe give @s iyc:stone_high_stool
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_bench":true} }] run recipe give @s iyc:oak_bench
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_bench":true} }] run recipe give @s iyc:birch_bench
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_bench":true} }] run recipe give @s iyc:cobblestone_bench
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_bench":true} }] run recipe give @s iyc:stone_bench
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_chair":true} }] run recipe give @s iyc:oak_chair
execute if items entity @s container.* *[custom_data~{"iyc": {"birch_chair":true} }] run recipe give @s iyc:birch_chair
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_chair":true} }] run recipe give @s iyc:cobblestone_chair
execute if items entity @s container.* *[custom_data~{"iyc": {"stone_chair":true} }] run recipe give @s iyc:stone_chair
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_shelf":true} }] run recipe give @s iyc:oak_shelf
execute if items entity @s container.* *[custom_data~{"iyc": {"oak_barrel":true} }] run recipe give @s iyc:oak_barrel
execute if items entity @s container.* *[custom_data~{"iyc": {"flatware":true} }] run recipe give @s iyc:flatware
execute if items entity @s container.* *[custom_data~{"iyc": {"nuclear_bomb":true} }] run recipe give @s iyc:nuclear_bomb
execute if items entity @s container.* *[custom_data~{"iyc": {"cobblestone_campfire":true} }] run recipe give @s iyc:cobblestone_campfire
execute if items entity @s container.* *[custom_data~{"iyc": {"brick_campfire":true} }] run recipe give @s iyc:brick_campfire
execute if items entity @s container.* *[custom_data~{"iyc": {"stonebrick_campfire":true} }] run recipe give @s iyc:stonebrick_campfire
execute if items entity @s container.* *[custom_data~{"iyc": {"sandstone_campfire":true} }] run recipe give @s iyc:sandstone_campfire
execute if items entity @s container.* *[custom_data~{"iyc": {"white_cloud":true} }] run recipe give @s iyc:white_cloud
execute if items entity @s container.* *[custom_data~{"iyc": {"blue_block_ctf":true} }] run recipe give @s iyc:blue_block_ctf
execute if items entity @s container.* *[custom_data~{"iyc": {"red_block_ctf":true} }] run recipe give @s iyc:red_block_ctf
execute if items entity @s container.* *[custom_data~{"iyc": {"iron_furnace":true} }] run recipe give @s iyc:iron_furnace

