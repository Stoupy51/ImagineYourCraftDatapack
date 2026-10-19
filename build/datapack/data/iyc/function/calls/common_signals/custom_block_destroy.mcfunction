
#> iyc:calls/common_signals/custom_block_destroy
#
# @executed	at @s & align xyz
#
# @within	#common_signals:signals/custom_block_destroy
#			iyc:calls/common_signals/on_ore_destroyed
#

execute as @e[tag=iyc.custom_block,dx=0,dy=0,dz=0] at @s run function iyc:custom_blocks/destroy

