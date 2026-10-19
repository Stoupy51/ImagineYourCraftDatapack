
#> iyc:shapes/apply/20
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_east/half_top
#			iyc:shapes/stairs_1/facing_north/half_top
#			iyc:shapes/solid_neighbour_14/bottom_true/east_true/north_false/south_false/top_true
#			iyc:shapes/solid_neighbour_14/bottom_true/east_true/north_false/south_false/top_false
#

execute if score @s iyc.shape matches 20 run return 0
scoreboard players set @s iyc.shape 20
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["20"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

