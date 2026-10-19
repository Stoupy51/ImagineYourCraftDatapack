
#> iyc:interaction/attacked
#
# @executed	as the player & at current position
#
# @within	advancement iyc:interaction/attacked
#

advancement revoke @s only iyc:interaction/attacked
execute store success score #break_drop iyc.data if entity @s[gamemode=!creative]
execute as @e[type=interaction,tag=iyc.interaction,distance=..8] if data entity @s attack at @s align xyz positioned ~0.5 ~0.5 ~0.5 run function iyc:interaction/break
scoreboard players set #break_drop iyc.data 0

