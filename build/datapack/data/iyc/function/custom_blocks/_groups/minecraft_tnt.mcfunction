
#> iyc:custom_blocks/_groups/minecraft_tnt
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_nuclear_bomb iyc.data matches 1.. if entity @s[tag=iyc.nuclear_bomb] run function iyc:custom_blocks/nuclear_bomb/destroy

