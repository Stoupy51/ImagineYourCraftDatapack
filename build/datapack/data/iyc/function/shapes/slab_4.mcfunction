
#> iyc:shapes/slab_4
#
# @executed	at @s
#
# @within	iyc:custom_blocks/netherrack_slab/place_secondary
#			iyc:custom_blocks/reversed_planks_slab/place_secondary
#			iyc:custom_blocks/obsidian_slab/place_secondary
#			iyc:custom_blocks/oak_log_slab/place_secondary
#			iyc:custom_blocks/glowstone_slab/place_secondary
#			iyc:custom_blocks/slate_slab/place_secondary
#			iyc:shapes/follow
#

execute if block ~ ~ ~ #iyc:hosts/slab[type=bottom] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/slab[type=top] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/slab[type=double] run return run function iyc:shapes/apply/2

