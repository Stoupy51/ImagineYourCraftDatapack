
#> iyc:custom_blocks/_groups/minecraft_ladder
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_iron_ladder iyc.data matches 1.. if entity @s[tag=iyc.iron_ladder] run function iyc:custom_blocks/iron_ladder/destroy

