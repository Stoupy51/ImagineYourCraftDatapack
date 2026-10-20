
#> iyc:custom_blocks/cobblestone_high_stool/sit
#
# @executed	at @s
#
# @within	iyc:custom_blocks/_interaction/use
#

execute as @p[tag=iyc.user] if predicate {"type": "minecraft:entity_properties","entity": "this","predicate": {"vehicle": {}}} run return fail
execute positioned ~ ~0.875 ~ summon item_display run function iyc:custom_blocks/_interaction/seat

