
#> iyc:shapes/apply/13
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_west/half_top
#			iyc:shapes/wall_8/east_false/north_true/south_true/up_false
#			iyc:shapes/wall_8/east_false/north_true/south_true/up_true
#			iyc:shapes/fence_9/east_false/north_true/south_true
#			iyc:shapes/gate_10/facing_west/in_wall_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_false/south_false/top_false
#			iyc:shapes/same_neighbour_17/east_false/north_true/south_true
#

execute if score @s iyc.shape matches 13 run return 0
scoreboard players set @s iyc.shape 13
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["13"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

