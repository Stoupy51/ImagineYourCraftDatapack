
#> iyc:custom_blocks/_groups/minecraft_nether_brick_fence
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_stone_fence iyc.data matches 1.. if entity @s[tag=iyc.stone_fence] run function iyc:custom_blocks/stone_fence/destroy
execute if score #total_white_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.white_iron_fence] run function iyc:custom_blocks/white_iron_fence/destroy
execute if score #total_orange_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.orange_iron_fence] run function iyc:custom_blocks/orange_iron_fence/destroy
execute if score #total_magenta_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.magenta_iron_fence] run function iyc:custom_blocks/magenta_iron_fence/destroy
execute if score #total_light_blue_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.light_blue_iron_fence] run function iyc:custom_blocks/light_blue_iron_fence/destroy
execute if score #total_yellow_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.yellow_iron_fence] run function iyc:custom_blocks/yellow_iron_fence/destroy
execute if score #total_lime_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.lime_iron_fence] run function iyc:custom_blocks/lime_iron_fence/destroy
execute if score #total_pink_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.pink_iron_fence] run function iyc:custom_blocks/pink_iron_fence/destroy
execute if score #total_gray_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.gray_iron_fence] run function iyc:custom_blocks/gray_iron_fence/destroy
execute if score #total_light_gray_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.light_gray_iron_fence] run function iyc:custom_blocks/light_gray_iron_fence/destroy
execute if score #total_cyan_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.cyan_iron_fence] run function iyc:custom_blocks/cyan_iron_fence/destroy
execute if score #total_purple_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.purple_iron_fence] run function iyc:custom_blocks/purple_iron_fence/destroy
execute if score #total_blue_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.blue_iron_fence] run function iyc:custom_blocks/blue_iron_fence/destroy
execute if score #total_brown_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.brown_iron_fence] run function iyc:custom_blocks/brown_iron_fence/destroy
execute if score #total_green_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.green_iron_fence] run function iyc:custom_blocks/green_iron_fence/destroy
execute if score #total_red_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.red_iron_fence] run function iyc:custom_blocks/red_iron_fence/destroy
execute if score #total_black_iron_fence iyc.data matches 1.. if entity @s[tag=iyc.black_iron_fence] run function iyc:custom_blocks/black_iron_fence/destroy

