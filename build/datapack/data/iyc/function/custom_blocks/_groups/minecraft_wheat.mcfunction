
#> iyc:custom_blocks/_groups/minecraft_wheat
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_hops_seeds iyc.data matches 1.. if entity @s[tag=iyc.hops_seeds] run function iyc:custom_blocks/hops_seeds/destroy

