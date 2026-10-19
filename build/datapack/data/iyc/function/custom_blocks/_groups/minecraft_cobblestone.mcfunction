
#> iyc:custom_blocks/_groups/minecraft_cobblestone
#
# @executed	as @e[type=item_display,tag=...,predicate=!iyc:check_vanilla_blocks] & at @s
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_black_smoke_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.black_smoke_effect_generator] run function iyc:custom_blocks/black_smoke_effect_generator/destroy
execute if score #total_portal_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.portal_effect_generator] run function iyc:custom_blocks/portal_effect_generator/destroy
execute if score #total_explosion_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.explosion_effect_generator] run function iyc:custom_blocks/explosion_effect_generator/destroy
execute if score #total_white_smoke_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.white_smoke_effect_generator] run function iyc:custom_blocks/white_smoke_effect_generator/destroy
execute if score #total_lava_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.lava_effect_generator] run function iyc:custom_blocks/lava_effect_generator/destroy
execute if score #total_water_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.water_effect_generator] run function iyc:custom_blocks/water_effect_generator/destroy
execute if score #total_big_black_smoke_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.big_black_smoke_effect_generator] run function iyc:custom_blocks/big_black_smoke_effect_generator/destroy
execute if score #total_heart_effect_generator iyc.data matches 1.. if entity @s[tag=iyc.heart_effect_generator] run function iyc:custom_blocks/heart_effect_generator/destroy

