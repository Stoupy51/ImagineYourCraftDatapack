
#> iyc:custom_blocks/hops_seeds/minute
#
# @executed	at @s
#
# @within	iyc:custom_blocks/minute
#

# Increment growth time score by 60 and update model
scoreboard players add @s iyc.growth_time 60
execute if score #boost_growth_time iyc.data matches 1.. run scoreboard players operation @s iyc.growth_time += #boost_growth_time iyc.data
function iyc:custom_blocks/hops_seeds/update_seed_model

