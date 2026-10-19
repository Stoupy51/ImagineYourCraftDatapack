
#> iyc:shapes/apply/36
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_true/south_true/top_true
#			iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_true/south_true/top_false
#

execute if score @s iyc.shape matches 36 run return 0
scoreboard players set @s iyc.shape 36
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["27"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

