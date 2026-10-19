
#> iyc:shapes/apply/31
#
# @executed	at @s
#
# @within	iyc:shapes/ladder_13
#			iyc:shapes/furnace_21/facing_south
#

execute if score @s iyc.shape matches 31 run return 0
scoreboard players set @s iyc.shape 31
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["1"]}}},transformation:{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

