
#> iyc:custom_blocks/_interaction/used
#
# @executed	as the player & at current position
#
# @within	advancement iyc:custom_blocks/interaction_used
#

advancement revoke @s only iyc:custom_blocks/interaction_used
tag @s add iyc.user
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s interaction at @s run function iyc:custom_blocks/_interaction/use
tag @s remove iyc.user

