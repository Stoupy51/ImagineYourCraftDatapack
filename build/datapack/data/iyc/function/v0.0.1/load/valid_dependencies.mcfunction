
#> iyc:v0.0.1/load/valid_dependencies
#
# @within	iyc:v0.0.1/load/secondary
#			iyc:v0.0.1/load/valid_dependencies 1t replace
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run schedule function iyc:v0.0.1/load/valid_dependencies 1t replace
execute unless entity @p run return 0
execute store result score #game_version iyc.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error iyc.data 0
execute unless score #game_version iyc.data matches 4321.. run scoreboard players set #mcload_error iyc.data 1

# Decode errors
execute if score #mcload_error iyc.data matches 1 run tellraw @a {"text":"ImagineYourCraft Error: This version is made for Minecraft 1.21.4+.","color":"red"}
execute if score #dependency_error iyc.data matches 1 run tellraw @a {"text":"ImagineYourCraft Error: Libraries are missing\nplease download the right ImagineYourCraft datapack\nor download each of these libraries one by one:","color":"red"}
execute if score #dependency_error iyc.data matches 1 unless score #common_signals.major load.status matches 0.. run tellraw @a {"text":"- [Common Signals (v0.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/CommonSignals"}}
execute if score #dependency_error iyc.data matches 1 if score #common_signals.major load.status matches 0 unless score #common_signals.minor load.status matches 1.. run tellraw @a {"text":"- [Common Signals (v0.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/CommonSignals"}}
execute if score #dependency_error iyc.data matches 1 unless score #smithed.custom_block.major load.status matches 0.. run tellraw @a {"text":"- [Smithed Custom Block (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/custom-block/"}}
execute if score #dependency_error iyc.data matches 1 if score #smithed.custom_block.major load.status matches 0 unless score #smithed.custom_block.minor load.status matches 6.. run tellraw @a {"text":"- [Smithed Custom Block (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/custom-block/"}}
execute if score #dependency_error iyc.data matches 1 if score #smithed.custom_block.major load.status matches 0 if score #smithed.custom_block.minor load.status matches 6 unless score #smithed.custom_block.patch load.status matches 2.. run tellraw @a {"text":"- [Smithed Custom Block (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/custom-block/"}}
execute if score #dependency_error iyc.data matches 1 unless score #smithed.crafter.major load.status matches 0.. run tellraw @a {"text":"- [Smithed Crafter (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/crafter/"}}
execute if score #dependency_error iyc.data matches 1 if score #smithed.crafter.major load.status matches 0 unless score #smithed.crafter.minor load.status matches 6.. run tellraw @a {"text":"- [Smithed Crafter (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/crafter/"}}
execute if score #dependency_error iyc.data matches 1 if score #smithed.crafter.major load.status matches 0 if score #smithed.crafter.minor load.status matches 6 unless score #smithed.crafter.patch load.status matches 2.. run tellraw @a {"text":"- [Smithed Crafter (v0.6.2+)]","color":"gold","click_event":{"action":"open_url","url":"https://wiki.smithed.dev/libraries/crafter/"}}
execute if score #dependency_error iyc.data matches 1 unless score #furnace_nbt_recipes.major load.status matches 1.. run tellraw @a {"text":"- [Furnace NBT Recipes (v1.9.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/FurnaceNbtRecipes"}}
execute if score #dependency_error iyc.data matches 1 if score #furnace_nbt_recipes.major load.status matches 1 unless score #furnace_nbt_recipes.minor load.status matches 9.. run tellraw @a {"text":"- [Furnace NBT Recipes (v1.9.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/FurnaceNbtRecipes"}}
execute if score #dependency_error iyc.data matches 1 unless score #smart_ore_generation.major load.status matches 1.. run tellraw @a {"text":"- [SmartOreGeneration (v1.7.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/SmartOreGeneration"}}
execute if score #dependency_error iyc.data matches 1 if score #smart_ore_generation.major load.status matches 1 unless score #smart_ore_generation.minor load.status matches 7.. run tellraw @a {"text":"- [SmartOreGeneration (v1.7.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/SmartOreGeneration"}}
execute if score #dependency_error iyc.data matches 1 if score #smart_ore_generation.major load.status matches 1 if score #smart_ore_generation.minor load.status matches 7 unless score #smart_ore_generation.patch load.status matches 1.. run tellraw @a {"text":"- [SmartOreGeneration (v1.7.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/SmartOreGeneration"}}

# Load ImagineYourCraft
execute if score #game_version iyc.data matches 1.. if score #mcload_error iyc.data matches 0 if score #dependency_error iyc.data matches 0 run function iyc:v0.0.1/load/confirm_load

