
#> iyc:interaction/break
#
# @executed	at @s & align xyz & positioned ~0.5 ~0.5 ~0.5
#
# @within	iyc:interaction/attacked [ at @s & align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#

setblock ~ ~ ~ air
execute as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] run function iyc:custom_blocks/destroy

