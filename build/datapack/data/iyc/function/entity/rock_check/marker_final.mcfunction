
#> iyc:entity/rock_check/marker_final
#
# @within	iyc:tick
#

# Tag the player who throwed the rock
scoreboard players set #success iyc.data 1
data modify storage iyc:main Owner set from entity @s data.Owner
execute as @a run function iyc:entity/rock_check/get_owner

# Damage the closest entity (by owner or at the rock position if no owner found)
execute as @p[tag=iyc.owner] run damage @e[type=#iyc:rock,tag=!smithed.strict,sort=nearest,limit=1,distance=..1.5,nbt=!{Invulnerable:1b}] 2.0 arrow by @s from @s
execute if score #success iyc.data matches 1 run damage @e[type=#iyc:rock,tag=!smithed.strict,sort=nearest,limit=1,distance=..1.5,nbt=!{Invulnerable:1b}] 2.0 arrow at ~ ~ ~

# Remove owner tag
execute if score #success iyc.data matches 0 run tag @p[tag=iyc.owner] remove iyc.owner

# Increment markers score to enable marker ticking
scoreboard players remove #rock_markers iyc.data 1
kill @s

