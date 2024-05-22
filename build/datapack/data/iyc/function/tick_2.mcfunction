
#> iyc:tick_2
#
# @within	iyc:tick
#

# Reset timer
scoreboard players set #tick_2 iyc.data 1

# 2 ticks destroy detection
execute as @e[type=item_display,tag=iyc.custom_block,tag=!iyc.vanilla.minecraft_polished_deepslate,predicate=!iyc:check_vanilla_blocks] at @s run function iyc:custom_blocks/destroy

