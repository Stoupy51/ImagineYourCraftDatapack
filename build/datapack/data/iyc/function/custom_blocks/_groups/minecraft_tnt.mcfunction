
#> iyc:custom_blocks/_groups/minecraft_tnt
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_nuclear_bomb iyc.data matches 1.. if entity @s[tag=iyc.nuclear_bomb] run function iyc:custom_blocks/nuclear_bomb/destroy

