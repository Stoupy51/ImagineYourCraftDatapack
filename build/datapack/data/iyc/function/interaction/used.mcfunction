
#> iyc:interaction/used
#
# @executed	as the player & at current position
#
# @within	advancement iyc:interaction/used
#

advancement revoke @s only iyc:interaction/used
tag @s add iyc.user
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s interaction at @s run function iyc:interaction/use
tag @s remove iyc.user

