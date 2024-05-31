
#> iyc:custom_blocks/get_rotation
#
# @within	iyc:custom_blocks/iron_furnace/place_main
#			iyc:custom_blocks/iron_ladder/place_main
#

# Set up score
scoreboard players set #rotation iyc.data 0

# Player case
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=-46..45] run scoreboard players set #rotation iyc.data 1
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=45..135] run scoreboard players set #rotation iyc.data 2
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=135..225] run scoreboard players set #rotation iyc.data 3
execute if score #rotation iyc.data matches 0 if entity @s[y_rotation=225..315] run scoreboard players set #rotation iyc.data 4

# Predicate case
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/north run scoreboard players set #rotation iyc.data 1
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/east run scoreboard players set #rotation iyc.data 2
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/south run scoreboard players set #rotation iyc.data 3
execute if score #rotation iyc.data matches 0 if predicate iyc:facing/west run scoreboard players set #rotation iyc.data 4
# No more cases for now

