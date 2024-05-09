
#> iyc:entity/rock_check/main
#
# @within	iyc:tick
#

# # Add tag to prevent function from running again
tag @s add iyc.rock_checked

# Stop function if not rock and if no owner
execute unless data entity @s Item.components."minecraft:custom_data".iyc.rock run return 0
execute unless data entity @s Owner run return 0

# Add a marker to track when the rock will disappear and track the owner
data modify storage iyc:main Owner set from entity @s Owner
tag @s add iyc.temp
execute at @s summon marker run function iyc:entity/rock_check/marker_setup
tag @s remove iyc.temp

