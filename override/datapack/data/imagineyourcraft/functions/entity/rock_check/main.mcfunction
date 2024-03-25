
# # Add tag to prevent function from running again
tag @s add imagineyourcraft.rock_checked

# Stop function if not rock and if no owner
execute unless data entity @s Item.components."minecraft:custom_data".imagineyourcraft.rock run return 0
execute unless data entity @s Owner run return 0

# Add a marker to track when the rock will disappear and track the owner
data modify storage imagineyourcraft:main Owner set from entity @s Owner
tag @s add imagineyourcraft.temp
execute at @s summon marker run function imagineyourcraft:entity/rock_check/marker_setup
tag @s remove imagineyourcraft.temp

