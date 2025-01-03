
#> iyc:calls/smithed_crafter/shapeless_recipes
#
# @within	#smithed.crafter:event/shapeless_recipes
#

execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"adamantium_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/adamantium_fragment_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"sapphire_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/sapphire_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"ruby_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/ruby_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"topaz_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/topaz_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"steel_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/steel_ingot_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"steel_ingot": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/steel_nugget_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"lignite_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/lignite_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"slate_block": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/slate_x9
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:obsidian", "count": 9}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/massive_obsidian_block
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:oak_planks", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"ruby": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/box_jump
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:oak_planks", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"sapphire": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/box_speed
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:iron_ingot", "count": 1}, {"id": "minecraft:arrow", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/bolt
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glass", "count": 9}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/clear_glass_x4
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:iron_ingot", "count": 1}, {"id": "minecraft:elytra", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/helice_hat
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glowstone", "count": 1}, {"id": "minecraft:birch_wood", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/birch_wood_lantern
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glowstone", "count": 1}, {"id": "minecraft:jungle_wood", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/jungle_wood_lantern
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glowstone", "count": 1}, {"id": "minecraft:oak_wood", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/oak_wood_lantern
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glowstone", "count": 1}, {"id": "minecraft:spruce_wood", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/spruce_wood_lantern
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:glowstone", "count": 1}, {"id": "minecraft:iron_block", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/iron_lantern
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:redstone_lamp", "count": 1}, {"id": "minecraft:red_wool", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/red_light
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:apple", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"empty_glass": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/apple_juice
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"beer_mug": true}}}}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"hops": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/beer
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"cherry": true}}}}, {"id": "minecraft:cake", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/cherry_cake
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 4 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"can": true}}}}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"cola": true}}}}, {"id": "minecraft:sugar", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"caffeine": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/coca
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 3 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:cocoa_beans", "count": 1}, {"id": "minecraft:bowl", "count": 1}, {"id": "minecraft:milk_bucket", "count": 1}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/hot_chocolate
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 4 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:cocoa_beans", "count": 3}, {"id": "minecraft:sugar", "count": 2}, {"id": "minecraft:milk_bucket", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"glass_pot": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/nutella
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 2 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"nutella": true}}}}, {"count": 4, "components": {"minecraft:custom_data": {"iyc": {"toast": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/nutella_toast_x4
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 4 if data storage smithed.crafter:input {"recipe": [{"count": 1, "components": {"minecraft:custom_data": {"iyc": {"can": true}}}}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"taurine": true}}}}, {"id": "minecraft:sugar", "count": 1}, {"count": 1, "components": {"minecraft:custom_data": {"iyc": {"caffeine": true}}}}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/red_bull
execute if score @s smithed.data matches 0 store result score @s smithed.data if score count smithed.data matches 1 if data storage smithed.crafter:input {"recipe": [{"id": "minecraft:chain", "count": 2}]} run loot replace block ~ ~ ~ container.16 loot iyc:i/chainmail_x4

