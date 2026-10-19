
#> iyc:custom_blocks/hops_seeds/place_check
#
# @executed	as @e[type=item_frame,tag=...] & at @s
#
# @within	iyc:custom_blocks/hops_seeds/search [ as @e[type=item_frame,tag=...] & at @s ]
#

# Check if there is air block at the position
execute if block ~ ~ ~ air run return run function iyc:custom_blocks/hops_seeds/place_main

# If not air, give back the item to the player
tag @e[type=item] add iyc.temp
execute as @p[tag=iyc.to_refund] at @s run loot spawn ~ ~ ~ loot iyc:i/hops_seeds
data merge entity @n[type=item,tag=!iyc.temp] {PickupDelay:0s,Motion:[0.0d,0.0d,0.0d]}
data modify entity @n[type=item,tag=!iyc.temp] Owner set from entity @p[tag=iyc.to_refund] UUID
tag @n[type=item] remove iyc.temp

# And kill the item frame
kill @s

