
#> iyc:advancements/unlock_recipes
#
# @within	advancement iyc:unlock_recipes
#

# Revoke advancement
advancement revoke @s only iyc:unlock_recipes

## For each ingredient in inventory, unlock the recipes
# minecraft:emerald
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:emerald
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_shovel
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_pickaxe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_sword
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_leggings
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_chestplate
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_helmet
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_boots
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_axe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_hoe

# minecraft:stick
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:stick
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_shovel
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_pickaxe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_sword
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_axe
execute if score #success iyc.data matches 1 run recipe give @s iyc:emerald_hoe

# minecraft:stone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:stone
execute if score #success iyc.data matches 1 run recipe give @s iyc:stone_stick

# minecraft:obsidian
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:obsidian
execute if score #success iyc.data matches 1 run recipe give @s iyc:massive_obsidian_block

# minecraft:iron_ingot
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:iron_ingot
execute if score #success iyc.data matches 1 run recipe give @s iyc:bolt
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_furnace
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_ladder
execute if score #success iyc.data matches 1 run recipe give @s iyc:helice_hat

# minecraft:furnace
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:furnace
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_furnace

# minecraft:blue_wool
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:blue_wool
execute if score #success iyc.data matches 1 run recipe give @s iyc:blue_block_ctf

# minecraft:glass
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:blue_block_ctf
execute if score #success iyc.data matches 1 run recipe give @s iyc:clear_glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:empty_glass
execute if score #success iyc.data matches 1 run recipe give @s iyc:beer_mug_2
execute if score #success iyc.data matches 1 run recipe give @s iyc:beer_mug
execute if score #success iyc.data matches 1 run recipe give @s iyc:glass_pot

# minecraft:arrow
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:arrow
execute if score #success iyc.data matches 1 run recipe give @s iyc:bolt

# minecraft:elytra
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:elytra
execute if score #success iyc.data matches 1 run recipe give @s iyc:helice_hat

# minecraft:glowstone
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:glowstone
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_wood_lantern
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_lantern

# minecraft:birch_wood
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:birch_wood
execute if score #success iyc.data matches 1 run recipe give @s iyc:birch_wood_lantern

# minecraft:jungle_wood
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:jungle_wood
execute if score #success iyc.data matches 1 run recipe give @s iyc:jungle_wood_lantern

# minecraft:oak_wood
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:oak_wood
execute if score #success iyc.data matches 1 run recipe give @s iyc:oak_wood_lantern

# minecraft:spruce_wood
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:spruce_wood
execute if score #success iyc.data matches 1 run recipe give @s iyc:spruce_wood_lantern

# minecraft:iron_block
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:iron_block
execute if score #success iyc.data matches 1 run recipe give @s iyc:iron_lantern

# minecraft:redstone_lamp
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:redstone_lamp
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_light

# minecraft:red_wool
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:red_wool
execute if score #success iyc.data matches 1 run recipe give @s iyc:red_light

# minecraft:oak_planks
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:oak_planks
execute if score #success iyc.data matches 1 run recipe give @s iyc:reversed_oak_planks

# minecraft:bread
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:bread
execute if score #success iyc.data matches 1 run recipe give @s iyc:toast

# minecraft:cocoa_beans
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:cocoa_beans
execute if score #success iyc.data matches 1 run recipe give @s iyc:hot_chocolate

# minecraft:bowl
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:bowl
execute if score #success iyc.data matches 1 run recipe give @s iyc:hot_chocolate

# minecraft:milk_bucket
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:milk_bucket
execute if score #success iyc.data matches 1 run recipe give @s iyc:hot_chocolate

# minecraft:chain
scoreboard players set #success iyc.data 0
execute store success score #success iyc.data if items entity @s container.* minecraft:chain
execute if score #success iyc.data matches 1 run recipe give @s iyc:chainmail

