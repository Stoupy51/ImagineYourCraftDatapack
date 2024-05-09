
#> iyc:second
#
# @within	iyc:tick
#

# Reset timer
scoreboard players set #second iyc.data 0

# 1 second break detection
execute as @e[type=item_display,tag=iyc.custom_block,tag=!iyc.vanilla.minecraft_polished_deepslate,predicate=!iyc:advanced_check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

