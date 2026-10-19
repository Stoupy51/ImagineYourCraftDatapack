
#> iyc:shapes/apply/5
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_west/half_bottom
#			iyc:shapes/stairs_1/facing_north/half_bottom
#			iyc:shapes/slope_2/facing_west
#			iyc:shapes/wall_8/east_true/north_true/south_false/up_false
#			iyc:shapes/wall_8/east_true/north_true/south_false/up_true
#			iyc:shapes/fence_9/east_true/north_true/south_false
#			iyc:shapes/gate_10/facing_west/in_wall_false
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_false
#			iyc:shapes/same_neighbour_15/east_true/north_true/south_false
#			iyc:shapes/same_neighbour_16/east_true/north_true/south_false
#			iyc:shapes/same_neighbour_17/east_true/north_true/south_false
#			iyc:shapes/brewing_22/has_bottle_0_true/has_bottle_1_false
#			iyc:shapes/cake_23
#

execute if score @s iyc.shape matches 5 run return 0
scoreboard players set @s iyc.shape 5
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["5"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

