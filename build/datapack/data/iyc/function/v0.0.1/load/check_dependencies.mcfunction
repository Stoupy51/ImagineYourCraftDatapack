
#> iyc:v0.0.1/load/check_dependencies
#
# @within	iyc:v0.0.1/load/secondary
#

## Check if ImagineYourCraft is loadable (dependencies)
scoreboard players set #dependency_error iyc.data 0
execute if score #dependency_error iyc.data matches 0 unless score #common_signals.major load.status matches 0.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #common_signals.major load.status matches 0 unless score #common_signals.minor load.status matches 1.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #smithed.custom_block.major load.status matches 0.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smithed.custom_block.major load.status matches 0 unless score #smithed.custom_block.minor load.status matches 6.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smithed.custom_block.major load.status matches 0 if score #smithed.custom_block.minor load.status matches 6 unless score #smithed.custom_block.patch load.status matches 2.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #smithed.crafter.major load.status matches 0.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smithed.crafter.major load.status matches 0 unless score #smithed.crafter.minor load.status matches 6.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smithed.crafter.major load.status matches 0 if score #smithed.crafter.minor load.status matches 6 unless score #smithed.crafter.patch load.status matches 2.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #furnace_nbt_recipes.major load.status matches 1.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #furnace_nbt_recipes.major load.status matches 1 unless score #furnace_nbt_recipes.minor load.status matches 9.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #smart_ore_generation.major load.status matches 1.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smart_ore_generation.major load.status matches 1 unless score #smart_ore_generation.minor load.status matches 7.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 if score #smart_ore_generation.major load.status matches 1 if score #smart_ore_generation.minor load.status matches 7 unless score #smart_ore_generation.patch load.status matches 1.. run scoreboard players set #dependency_error iyc.data 1

