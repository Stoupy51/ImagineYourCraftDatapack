
#> iyc:custom_blocks/oak_high_stool/hit
#
# @executed	at @s & positioned ~ ~0.5 ~
#
# @within	iyc:custom_blocks/_interaction/dispatch_hit [ at @s & positioned ~ ~0.5 ~ ]
#

# A hit coming 20 ticks or more after the previous one starts the count again
particle minecraft:item{item:{id:"minecraft:furnace",components:{"minecraft:item_model":"iyc:oak_high_stool"}}} ~ ~ ~ 0.25 0.25 0.25 0.05 8
playsound minecraft:block.wood.hit block @a ~ ~ ~ 0.4
execute unless score @s iyc.last_hit matches -2147483648.. run scoreboard players set @s iyc.last_hit 0
execute store result score #now iyc.data run time query gametime
scoreboard players operation #elapsed iyc.data = #now iyc.data
scoreboard players operation #elapsed iyc.data -= @s iyc.last_hit
execute if score #elapsed iyc.data matches 20.. run scoreboard players set @s iyc.hits 0
scoreboard players operation @s iyc.last_hit = #now iyc.data
scoreboard players add @s iyc.hits 1
execute unless entity @p[tag=iyc.breaker,gamemode=creative] if score @s iyc.hits matches ..2 run return 0

# Break it, dropping nothing for a creative player
execute store success score #no_drop iyc.data if entity @p[tag=iyc.breaker,gamemode=creative]
function iyc:custom_blocks/_interaction/break

