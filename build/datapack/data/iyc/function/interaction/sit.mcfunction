
#> iyc:interaction/sit
#
# @executed	at @s
#
# @within	iyc:interaction/use {height:0.5}
#			iyc:interaction/use {height:0.59}
#			iyc:interaction/use {height:0.875}
#
# @args		height (double)
#

$execute positioned ~ ~$(height) ~ summon item_display run tag @s add iyc.seat
ride @p[tag=iyc.user] mount @n[type=item_display,tag=iyc.seat]

