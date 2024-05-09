
#> iyc:load/check_dependencies
#
# @within	iyc:load/secondary
#

## Check if ImagineYourCraft is loadable (dependencies)
scoreboard players set #dependency_error iyc.data 0
execute if score #dependency_error iyc.data matches 0 unless score #common_signals.major load.status matches 0.. unless score #common_signals.minor load.status matches 0.. unless score #common_signals.patch load.status matches 0.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #smithed.custom_block.major load.status matches 0.. unless score #smithed.custom_block.minor load.status matches 3.. unless score #smithed.custom_block.patch load.status matches 0.. run scoreboard players set #dependency_error iyc.data 1
execute if score #dependency_error iyc.data matches 0 unless score #smithed.crafter.major load.status matches 0.. unless score #smithed.crafter.minor load.status matches 3.. unless score #smithed.crafter.patch load.status matches 1.. run scoreboard players set #dependency_error iyc.data 1

