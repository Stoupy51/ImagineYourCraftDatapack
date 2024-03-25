
# Tag the player who throwed the rock
scoreboard players set #success imagineyourcraft.data 1
data modify storage imagineyourcraft:main Owner set from entity @s data.Owner
execute as @a run function imagineyourcraft:entity/rock_check/get_owner

# Damage the closest entity (by owner or at the rock position if no owner found)
execute as @p[tag=imagineyourcraft.owner] run damage @e[type=#imagineyourcraft:rock,tag=!smithed.strict,sort=nearest,limit=1,distance=..1.5,nbt=!{Invulnerable:1b}] 2.0 arrow by @s from @s
execute if score #success imagineyourcraft.data matches 1 run damage @e[type=#imagineyourcraft:rock,tag=!smithed.strict,sort=nearest,limit=1,distance=..1.5,nbt=!{Invulnerable:1b}] 2.0 arrow at ~ ~ ~

# Remove owner tag
execute if score #success imagineyourcraft.data matches 0 run tag @p[tag=imagineyourcraft.owner] remove imagineyourcraft.owner

# Increment markers score to enable marker ticking
scoreboard players remove #rock_markers imagineyourcraft.data 1
kill @s

