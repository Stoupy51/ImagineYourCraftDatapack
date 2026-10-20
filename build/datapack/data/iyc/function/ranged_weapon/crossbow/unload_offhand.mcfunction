
#> iyc:ranged_weapon/crossbow/unload_offhand
#
# @executed	as the player & at current position
#
# @within	iyc:ranged_weapon/crossbow/loaded
#

# Give back what it loaded, unless the player is in creative where loading costs nothing
execute if entity @s[gamemode=!creative] run summon item ~ ~1 ~ {Item:{id:"minecraft:stone"},Tags:["iyc.unloaded"],PickupDelay:0s}
execute if entity @s[gamemode=!creative] run data modify entity @n[type=item,tag=iyc.unloaded] Item set from entity @s equipment.offhand.components."minecraft:charged_projectiles"[0]
tag @n[type=item,tag=iyc.unloaded] remove iyc.unloaded
item modify entity @s weapon.offhand {"type": "minecraft:set_components","components": {"minecraft:charged_projectiles": []}}

