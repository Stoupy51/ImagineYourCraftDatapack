
#> iyc:v0.0.1/second_5
#
# @within	iyc:v0.0.1/tick
#

# Reset timer
scoreboard players set #second_5 iyc.data -10

# 5 seconds break detection
execute if score #total_custom_blocks iyc.data matches 1.. as @e[type=item_display,tag=iyc.custom_block,predicate=!iyc:advanced_check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

