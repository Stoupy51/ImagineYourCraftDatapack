
#> iyc:custom_blocks/hops_seeds/place_main
#
# @executed	as @e[type=item_frame,tag=...] & at @s
#
# @within	iyc:custom_blocks/hops_seeds/place_check
#			iyc:interaction/light
#

tag @s add iyc.placer
setblock ~ ~ ~ air strict
setblock ~ ~ ~ minecraft:wheat
execute align xyz positioned ~0.5 ~0.5 ~0.5 summon item_display at @s run function iyc:custom_blocks/hops_seeds/place_secondary
tag @s remove iyc.placer

# Increment count scores
scoreboard players add #total_custom_blocks iyc.data 1
scoreboard players add #total_vanilla_wheat iyc.data 1
scoreboard players add #total_hops_seeds iyc.data 1
scoreboard players add #total_growing_seeds iyc.data 1
kill @s[type=item_frame]

