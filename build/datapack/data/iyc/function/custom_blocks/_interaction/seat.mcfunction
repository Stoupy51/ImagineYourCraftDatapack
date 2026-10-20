
#> iyc:custom_blocks/_interaction/seat
#
# @executed	positioned ~ ~0.59 ~
#
# @within	iyc:custom_blocks/oak_stool/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/birch_stool/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/cobblestone_stool/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/stone_stool/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/oak_high_stool/sit [ positioned ~ ~0.875 ~ ]
#			iyc:custom_blocks/birch_high_stool/sit [ positioned ~ ~0.875 ~ ]
#			iyc:custom_blocks/cobblestone_high_stool/sit [ positioned ~ ~0.875 ~ ]
#			iyc:custom_blocks/stone_high_stool/sit [ positioned ~ ~0.875 ~ ]
#			iyc:custom_blocks/oak_bench/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/birch_bench/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/cobblestone_bench/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/stone_bench/sit [ positioned ~ ~0.59 ~ ]
#			iyc:custom_blocks/oak_chair/sit [ positioned ~ ~0.5 ~ ]
#			iyc:custom_blocks/birch_chair/sit [ positioned ~ ~0.5 ~ ]
#			iyc:custom_blocks/cobblestone_chair/sit [ positioned ~ ~0.5 ~ ]
#			iyc:custom_blocks/stone_chair/sit [ positioned ~ ~0.5 ~ ]
#

tag @s add global.ignore
tag @s add global.ignore.kill
tag @s add smithed.entity
tag @s add iyc.seat
ride @p[tag=iyc.user] mount @s
scoreboard players add #seats iyc.data 1

