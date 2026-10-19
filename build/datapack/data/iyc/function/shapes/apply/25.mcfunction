
#> iyc:shapes/apply/25
#
# @executed	at @s
#
# @within	iyc:shapes/trapdoor_5/facing_east/half_bottom
#			iyc:shapes/trapdoor_5/facing_east/half_top
#

execute if score @s iyc.shape matches 25 run return 0
scoreboard players set @s iyc.shape 25
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["2"]}}},transformation:{left_rotation:[0.0f,0.7071068f,0.0f,0.7071068f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

