
#> iyc:shapes/apply/29
#
# @executed	at @s
#
# @within	iyc:shapes/ladder_7
#			iyc:shapes/facing_away_18
#			iyc:shapes/facing_player_19
#			iyc:shapes/furnace_21/facing_west
#

execute if score @s iyc.shape matches 29 run return 0
scoreboard players set @s iyc.shape 29
data merge entity @s {Rotation:[0.0f,0.0f],item:{components:{"minecraft:custom_model_data":{strings:["0"]}}},transformation:{left_rotation:[0.0f,-0.7071068f,0.0f,0.7071068f],right_rotation:[0.0f,0.0f,0.0f,1.0f],translation:[0f,0f,0f],scale:[1f,1f,1f]}}

