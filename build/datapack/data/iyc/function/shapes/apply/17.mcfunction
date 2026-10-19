
#> iyc:shapes/apply/17
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_west/half_top
#			iyc:shapes/stairs_1/facing_south/half_top
#			iyc:shapes/wall_8/east_true/north_false/south_false/up_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_true/south_false/top_true
#			iyc:shapes/solid_neighbour_14/bottom_false/east_true/north_true/south_false/top_false
#

execute if score @s iyc.shape matches 17 run return 0
scoreboard players set @s iyc.shape 17
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["17"]}}},transformation:{left_rotation:[0.0f,1.0f,0.0f,0.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

