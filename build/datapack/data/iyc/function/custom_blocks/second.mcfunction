
#> iyc:custom_blocks/second
#
# @executed	as @e[tag=iyc.second] & at @s
#
# @within	iyc:v0.1.0/second [ as @e[tag=iyc.second] & at @s ]
#

execute if entity @s[tag=iyc.black_smoke_effect_generator] run function iyc:custom_blocks/black_smoke_effect_generator/second
execute if entity @s[tag=iyc.portal_effect_generator] run function iyc:custom_blocks/portal_effect_generator/second
execute if entity @s[tag=iyc.explosion_effect_generator] run function iyc:custom_blocks/explosion_effect_generator/second
execute if entity @s[tag=iyc.white_smoke_effect_generator] run function iyc:custom_blocks/white_smoke_effect_generator/second
execute if entity @s[tag=iyc.lava_effect_generator] run function iyc:custom_blocks/lava_effect_generator/second
execute if entity @s[tag=iyc.water_effect_generator] run function iyc:custom_blocks/water_effect_generator/second
execute if entity @s[tag=iyc.big_black_smoke_effect_generator] run function iyc:custom_blocks/big_black_smoke_effect_generator/second
execute if entity @s[tag=iyc.heart_effect_generator] run function iyc:custom_blocks/heart_effect_generator/second

