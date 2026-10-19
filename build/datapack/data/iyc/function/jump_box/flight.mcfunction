
#> iyc:jump_box/flight
#
# @executed	as @a[tag=iyc.launched]
#
# @within	iyc:v0.1.0/tick [ as @a[tag=iyc.launched] ]
#

scoreboard players remove @s iyc.jump 1
execute if score @s iyc.jump matches 0 run effect clear @s minecraft:levitation
execute if score @s iyc.jump matches ..-5 if predicate {type:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_on_ground:true}}} run function iyc:jump_box/landed

