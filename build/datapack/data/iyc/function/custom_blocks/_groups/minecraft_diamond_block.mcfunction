
#> iyc:custom_blocks/_groups/minecraft_diamond_block
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_sapphire_block iyc.data matches 1.. if entity @s[tag=iyc.sapphire_block] run function iyc:custom_blocks/sapphire_block/destroy
execute if score #total_ruby_block iyc.data matches 1.. if entity @s[tag=iyc.ruby_block] run function iyc:custom_blocks/ruby_block/destroy
execute if score #total_topaz_block iyc.data matches 1.. if entity @s[tag=iyc.topaz_block] run function iyc:custom_blocks/topaz_block/destroy

