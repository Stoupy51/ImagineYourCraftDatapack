
#> iyc:v0.1.0/second_5
#
# @within	iyc:v0.1.0/tick
#

# Reset timer
scoreboard players set #second_5 iyc.data -10

# 5 seconds break detection (item display only)
execute if score #total_custom_blocks iyc.data matches 1.. as @e[type=item_display,tag=iyc.custom_block,predicate=!iyc:advanced_check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

# 5 seconds growing seed break detection (below block check)
execute if score #total_growing_seeds iyc.data matches 1.. as @e[type=#iyc:custom_blocks,tag=iyc.growing_seed] at @s run function iyc:custom_blocks/destroy_growing_seeds

# 5 seconds dynamic brightness update (random sample of item_display custom blocks)
execute if score #total_custom_blocks iyc.data matches 1.. as @e[type=item_display,tag=iyc.custom_block,sort=random,limit=50] at @s run function iyc:custom_blocks/compute_brightness

