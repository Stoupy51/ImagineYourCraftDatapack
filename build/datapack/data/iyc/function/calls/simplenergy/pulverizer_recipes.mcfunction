
#> iyc:calls/simplenergy/pulverizer_recipes
#
# @within	#simplenergy:calls/pulverizer_recipes
#

execute if score #found simplenergy.data matches 0 store result score #found simplenergy.data if data storage simplenergy:main pulverizer.input{"components": {"minecraft:custom_data": {"iyc": {"steel_ingot": true}}}} run loot replace entity @s contents loot iyc:i/steel_dust
execute if score #found simplenergy.data matches 0 store result score #found simplenergy.data if data storage simplenergy:main pulverizer.input{"components": {"minecraft:custom_data": {"iyc": {"raw_steel": true}}}} run loot replace entity @s contents loot iyc:i/steel_dust_x2
execute if score #found simplenergy.data matches 0 store result score #found simplenergy.data if data storage simplenergy:main pulverizer.input{"components": {"minecraft:custom_data": {"iyc": {"steel_ore": true}}}} run loot replace entity @s contents loot iyc:i/steel_dust_x2
execute if score #found simplenergy.data matches 0 store result score #found simplenergy.data if data storage simplenergy:main pulverizer.input{"components": {"minecraft:custom_data": {"iyc": {"deepslate_steel_ore": true}}}} run loot replace entity @s contents loot iyc:i/steel_dust_x2

