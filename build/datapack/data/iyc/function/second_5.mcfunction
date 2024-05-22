
#> iyc:second_5
#
# @within	iyc:tick
#

# Reset timer
scoreboard players set #second_5 iyc.data -10

# 5 seconds break detection
execute as @e[type=item_display,tag=iyc.custom_block,predicate=!iyc:advanced_check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

