
#> iyc:custom_blocks/_groups/minecraft_barrel
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_oak_barrel iyc.data matches 1.. if entity @s[tag=iyc.oak_barrel] run function iyc:custom_blocks/oak_barrel/destroy

