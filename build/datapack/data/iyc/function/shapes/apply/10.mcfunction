
#> iyc:shapes/apply/10
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_west/half_bottom
#			iyc:shapes/stairs_1/facing_south/half_bottom
#			iyc:shapes/wall_8/east_true/north_false/south_false/up_false
#			iyc:shapes/fence_9/east_true/north_false/south_false
#			iyc:shapes/gate_10/facing_north/in_wall_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_false/south_true/top_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_false/north_false/south_true/top_false
#			iyc:shapes/same_neighbour_17/east_true/north_false/south_false
#

execute if score @s iyc.shape matches 10 run return 0
scoreboard players set @s iyc.shape 10
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["10"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

