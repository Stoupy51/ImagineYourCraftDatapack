
#> iyc:custom_blocks/_groups/minecraft_polished_deepslate
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_adamantium_ore iyc.data matches 1.. if entity @s[tag=iyc.adamantium_ore] run function iyc:custom_blocks/adamantium_ore/destroy
execute if score #total_deepslate_adamantium_ore iyc.data matches 1.. if entity @s[tag=iyc.deepslate_adamantium_ore] run function iyc:custom_blocks/deepslate_adamantium_ore/destroy
execute if score #total_sapphire_ore iyc.data matches 1.. if entity @s[tag=iyc.sapphire_ore] run function iyc:custom_blocks/sapphire_ore/destroy
execute if score #total_deepslate_sapphire_ore iyc.data matches 1.. if entity @s[tag=iyc.deepslate_sapphire_ore] run function iyc:custom_blocks/deepslate_sapphire_ore/destroy
execute if score #total_ruby_ore iyc.data matches 1.. if entity @s[tag=iyc.ruby_ore] run function iyc:custom_blocks/ruby_ore/destroy
execute if score #total_deepslate_ruby_ore iyc.data matches 1.. if entity @s[tag=iyc.deepslate_ruby_ore] run function iyc:custom_blocks/deepslate_ruby_ore/destroy
execute if score #total_topaz_ore iyc.data matches 1.. if entity @s[tag=iyc.topaz_ore] run function iyc:custom_blocks/topaz_ore/destroy
execute if score #total_deepslate_topaz_ore iyc.data matches 1.. if entity @s[tag=iyc.deepslate_topaz_ore] run function iyc:custom_blocks/deepslate_topaz_ore/destroy
execute if score #total_steel_ore iyc.data matches 1.. if entity @s[tag=iyc.steel_ore] run function iyc:custom_blocks/steel_ore/destroy
execute if score #total_deepslate_steel_ore iyc.data matches 1.. if entity @s[tag=iyc.deepslate_steel_ore] run function iyc:custom_blocks/deepslate_steel_ore/destroy
execute if score #total_lignite_ore iyc.data matches 1.. if entity @s[tag=iyc.lignite_ore] run function iyc:custom_blocks/lignite_ore/destroy
execute if score #total_slate_ore iyc.data matches 1.. if entity @s[tag=iyc.slate_ore] run function iyc:custom_blocks/slate_ore/destroy

