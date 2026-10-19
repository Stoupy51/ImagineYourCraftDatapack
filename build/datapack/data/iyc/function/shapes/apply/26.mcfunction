
#> iyc:shapes/apply/26
#
# @executed	at @s
#
# @within	iyc:shapes/trapdoor_5/facing_west/half_bottom
#			iyc:shapes/trapdoor_5/facing_west/half_top
#

execute if score @s iyc.shape matches 26 run return 0
scoreboard players set @s iyc.shape 26
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["2"]}}},transformation:{left_rotation:[0.0f,-0.7071068f,0.0f,0.7071068f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

