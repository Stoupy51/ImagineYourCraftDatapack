
#> iyc:flowers/effect
#
# @executed	as @a[gamemode=!spectator] & at @s
#
# @within	iyc:flowers/touch {effect:"poison"}
#			iyc:flowers/touch {effect:"slowness"}
#
# @args		effect (string)
#

$execute if score #difficulty iyc.data matches ..1 run effect give @s minecraft:$(effect) 5 0
$execute if score #difficulty iyc.data matches 2 run effect give @s minecraft:$(effect) 8 0
$execute if score #difficulty iyc.data matches 3 run effect give @s minecraft:$(effect) 15 0

