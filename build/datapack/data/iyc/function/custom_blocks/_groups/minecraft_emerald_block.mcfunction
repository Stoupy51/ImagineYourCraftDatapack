
#> iyc:custom_blocks/_groups/minecraft_emerald_block
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_lignite_block iyc.data matches 1.. if entity @s[tag=iyc.lignite_block] run function iyc:custom_blocks/lignite_block/destroy
execute if score #total_slate_block iyc.data matches 1.. if entity @s[tag=iyc.slate_block] run function iyc:custom_blocks/slate_block/destroy

