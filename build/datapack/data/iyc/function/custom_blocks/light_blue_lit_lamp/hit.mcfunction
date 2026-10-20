
#> iyc:custom_blocks/light_blue_lit_lamp/hit
#
# @executed	at @s & positioned ~ ~0.5 ~
#
# @within	iyc:custom_blocks/_interaction/dispatch_hit [ at @s & positioned ~ ~0.5 ~ ]
#

# Break it, dropping nothing for a creative player
execute store success score #no_drop iyc.data if entity @p[tag=iyc.breaker,gamemode=creative]
function iyc:custom_blocks/_interaction/break

