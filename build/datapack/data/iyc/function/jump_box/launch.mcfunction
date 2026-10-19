
#> iyc:jump_box/launch
#
# @executed	positioned ~-0.5 ~0.5 ~-0.5 & as @a[dx=0,dy=0,dz=0,tag=!iyc.launched,gamemode=!spectator]
#
# @within	iyc:custom_blocks/box_jump/tick [ positioned ~-0.5 ~0.5 ~-0.5 & as @a[dx=0,dy=0,dz=0,tag=!iyc.launched,gamemode=!spectator] ]
#

# Players move on their own client, so they are lifted by levitation: 4 ticks at amplifier 127 end near the 4 blocks per tick mobs get
playsound minecraft:block.piston.extend block @a ~ ~ ~ 0.5 0.7
effect give @s minecraft:levitation 1 127 true
attribute @s minecraft:safe_fall_distance modifier add iyc:jump_box 72 add_value
scoreboard players set @s iyc.jump 4
tag @s add iyc.launched

