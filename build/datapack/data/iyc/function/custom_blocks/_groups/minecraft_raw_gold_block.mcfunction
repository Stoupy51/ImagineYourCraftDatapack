
#> iyc:custom_blocks/_groups/minecraft_raw_gold_block
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_raw_steel_block iyc.data matches 1.. if entity @s[tag=iyc.raw_steel_block] run function iyc:custom_blocks/raw_steel_block/destroy

