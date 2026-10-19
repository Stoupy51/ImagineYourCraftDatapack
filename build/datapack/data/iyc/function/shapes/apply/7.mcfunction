
#> iyc:shapes/apply/7
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_east/half_bottom
#			iyc:shapes/stairs_1/facing_north/half_bottom
#			iyc:shapes/slope_2/facing_north
#			iyc:shapes/wall_8/east_false/north_false/south_true/up_false
#			iyc:shapes/wall_8/east_false/north_false/south_true/up_true
#			iyc:shapes/fence_9/east_false/north_false/south_true
#			iyc:shapes/gate_10/facing_east/in_wall_false
#			iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_false/south_false/top_false
#			iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_false/south_false/top_true
#			iyc:shapes/same_neighbour_15/east_false/north_false/south_true
#			iyc:shapes/same_neighbour_16/east_false/north_false/south_true
#			iyc:shapes/same_neighbour_17/east_false/north_false/south_true
#			iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_true
#

execute if score @s iyc.shape matches 7 run return 0
scoreboard players set @s iyc.shape 7
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["7"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

