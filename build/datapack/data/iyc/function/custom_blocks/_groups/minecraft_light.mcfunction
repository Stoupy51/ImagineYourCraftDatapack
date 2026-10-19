
#> iyc:custom_blocks/_groups/minecraft_light
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_transparent_light_block iyc.data matches 1.. if entity @s[tag=iyc.transparent_light_block] run function iyc:custom_blocks/transparent_light_block/destroy
execute if score #total_white_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.white_lit_lamp] run function iyc:custom_blocks/white_lit_lamp/destroy
execute if score #total_orange_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.orange_lit_lamp] run function iyc:custom_blocks/orange_lit_lamp/destroy
execute if score #total_magenta_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.magenta_lit_lamp] run function iyc:custom_blocks/magenta_lit_lamp/destroy
execute if score #total_light_blue_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.light_blue_lit_lamp] run function iyc:custom_blocks/light_blue_lit_lamp/destroy
execute if score #total_yellow_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.yellow_lit_lamp] run function iyc:custom_blocks/yellow_lit_lamp/destroy
execute if score #total_lime_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.lime_lit_lamp] run function iyc:custom_blocks/lime_lit_lamp/destroy
execute if score #total_pink_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.pink_lit_lamp] run function iyc:custom_blocks/pink_lit_lamp/destroy
execute if score #total_gray_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.gray_lit_lamp] run function iyc:custom_blocks/gray_lit_lamp/destroy
execute if score #total_light_gray_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.light_gray_lit_lamp] run function iyc:custom_blocks/light_gray_lit_lamp/destroy
execute if score #total_cyan_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.cyan_lit_lamp] run function iyc:custom_blocks/cyan_lit_lamp/destroy
execute if score #total_purple_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.purple_lit_lamp] run function iyc:custom_blocks/purple_lit_lamp/destroy
execute if score #total_blue_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.blue_lit_lamp] run function iyc:custom_blocks/blue_lit_lamp/destroy
execute if score #total_brown_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.brown_lit_lamp] run function iyc:custom_blocks/brown_lit_lamp/destroy
execute if score #total_green_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.green_lit_lamp] run function iyc:custom_blocks/green_lit_lamp/destroy
execute if score #total_red_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.red_lit_lamp] run function iyc:custom_blocks/red_lit_lamp/destroy
execute if score #total_black_lit_lamp iyc.data matches 1.. if entity @s[tag=iyc.black_lit_lamp] run function iyc:custom_blocks/black_lit_lamp/destroy

