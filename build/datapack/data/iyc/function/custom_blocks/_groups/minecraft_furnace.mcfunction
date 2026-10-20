
#> iyc:custom_blocks/_groups/minecraft_furnace
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_iron_furnace iyc.data matches 1.. if entity @s[tag=iyc.iron_furnace] run function iyc:custom_blocks/iron_furnace/destroy

