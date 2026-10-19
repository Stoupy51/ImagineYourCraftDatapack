
#> iyc:shapes/apply/34
#
# @executed	at @s
#
# @within	iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_false/south_true/top_true
#			iyc:shapes/solid_neighbour_14/bottom_true/east_false/north_false/south_true/top_false
#

execute if score @s iyc.shape matches 34 run return 0
scoreboard players set @s iyc.shape 34
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["25"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

