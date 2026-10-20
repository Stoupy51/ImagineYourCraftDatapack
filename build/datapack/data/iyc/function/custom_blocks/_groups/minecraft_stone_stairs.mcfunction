
#> iyc:custom_blocks/_groups/minecraft_stone_stairs
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_obsidian_stairs iyc.data matches 1.. if entity @s[tag=iyc.obsidian_stairs] run function iyc:custom_blocks/obsidian_stairs/destroy
execute if score #total_step_stairs iyc.data matches 1.. if entity @s[tag=iyc.step_stairs] run function iyc:custom_blocks/step_stairs/destroy
execute if score #total_slate_stairs iyc.data matches 1.. if entity @s[tag=iyc.slate_stairs] run function iyc:custom_blocks/slate_stairs/destroy

