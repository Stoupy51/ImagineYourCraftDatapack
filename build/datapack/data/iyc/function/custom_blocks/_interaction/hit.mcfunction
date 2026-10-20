
#> iyc:custom_blocks/_interaction/hit
#
# @executed	as the player & at current position
#
# @within	advancement iyc:custom_blocks/interaction_hit
#

advancement revoke @s only iyc:custom_blocks/interaction_hit
tag @s add iyc.breaker
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s attack run function iyc:custom_blocks/_interaction/dispatch_hit
tag @s remove iyc.breaker

