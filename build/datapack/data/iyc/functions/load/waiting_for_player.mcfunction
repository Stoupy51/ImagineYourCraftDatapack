
#> iyc:load/waiting_for_player
#
# @within	iyc:load/secondary
#			iyc:load/waiting_for_player 1t replace
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run schedule function iyc:load/waiting_for_player 1t replace
execute unless entity @p run return 0
execute store result score #game_version iyc.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error iyc.data 0
execute unless score #game_version iyc.data matches 3835.. run scoreboard players set #mcload_error iyc.data 1

# Decode errors
execute if score #mcload_error iyc.data matches 1 run tellraw @a {"translate":"iyc.imagineyourcraft_error_this_version_is_made_for_minecraft_1_20_6","color":"red"}
execute if score #dependency_error iyc.data matches 1 run tellraw @a {"translate":"iyc.imagineyourcraft_error_libraries_are_missingplease_download_the","color":"red"}
execute if score #dependency_error iyc.data matches 1 unless score #common_signals.major load.status matches 0.. unless score #common_signals.minor load.status matches 0.. unless score #common_signals.patch load.status matches 0.. run tellraw @a {"translate":"iyc.common_signals","color":"gold","clickEvent":{"action":"open_url","value":"https://github.com/Stoupy51/CommonSignals"}}
execute if score #dependency_error iyc.data matches 1 unless score #smithed.custom_block.major load.status matches 0.. unless score #smithed.custom_block.minor load.status matches 3.. unless score #smithed.custom_block.patch load.status matches 0.. run tellraw @a {"translate":"iyc.smithed_custom_block_placement","color":"gold","clickEvent":{"action":"open_url","value":"https://wiki.smithed.dev/libraries/custom-block/"}}

# Load ImagineYourCraft
execute if score #game_version iyc.data matches 1.. if score #mcload_error iyc.data matches 0 if score #dependency_error iyc.data matches 0 run function iyc:load/confirm_load

