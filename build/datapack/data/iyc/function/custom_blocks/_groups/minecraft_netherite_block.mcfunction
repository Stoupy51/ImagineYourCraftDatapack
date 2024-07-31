
#> iyc:custom_blocks/_groups/minecraft_netherite_block
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_adamantium_block iyc.data matches 1.. if entity @s[tag=iyc.adamantium_block] run function iyc:custom_blocks/adamantium_block/destroy
execute if score #total_massive_obsidian_block iyc.data matches 1.. if entity @s[tag=iyc.massive_obsidian_block] run function iyc:custom_blocks/massive_obsidian_block/destroy

