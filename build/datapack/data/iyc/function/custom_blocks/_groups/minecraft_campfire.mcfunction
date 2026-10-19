
#> iyc:custom_blocks/_groups/minecraft_campfire
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_cobblestone_campfire iyc.data matches 1.. if entity @s[tag=iyc.cobblestone_campfire] run function iyc:custom_blocks/cobblestone_campfire/destroy
execute if score #total_stone_campfire iyc.data matches 1.. if entity @s[tag=iyc.stone_campfire] run function iyc:custom_blocks/stone_campfire/destroy
execute if score #total_brick_campfire iyc.data matches 1.. if entity @s[tag=iyc.brick_campfire] run function iyc:custom_blocks/brick_campfire/destroy
execute if score #total_stonebrick_campfire iyc.data matches 1.. if entity @s[tag=iyc.stonebrick_campfire] run function iyc:custom_blocks/stonebrick_campfire/destroy
execute if score #total_sandstone_campfire iyc.data matches 1.. if entity @s[tag=iyc.sandstone_campfire] run function iyc:custom_blocks/sandstone_campfire/destroy

