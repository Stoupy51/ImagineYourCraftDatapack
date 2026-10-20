
#> iyc:custom_blocks/_groups/minecraft_diamond_block
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_sapphire_block iyc.data matches 1.. if entity @s[tag=iyc.sapphire_block] run function iyc:custom_blocks/sapphire_block/destroy
execute if score #total_ruby_block iyc.data matches 1.. if entity @s[tag=iyc.ruby_block] run function iyc:custom_blocks/ruby_block/destroy
execute if score #total_topaz_block iyc.data matches 1.. if entity @s[tag=iyc.topaz_block] run function iyc:custom_blocks/topaz_block/destroy
execute if score #total_adamantium_block iyc.data matches 1.. if entity @s[tag=iyc.adamantium_block] run function iyc:custom_blocks/adamantium_block/destroy
execute if score #total_massive_obsidian_block iyc.data matches 1.. if entity @s[tag=iyc.massive_obsidian_block] run function iyc:custom_blocks/massive_obsidian_block/destroy

