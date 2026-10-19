
#> iyc:custom_blocks/check_light
#
# @executed	positioned ~ ~1 ~
#
# @within	iyc:custom_blocks/compute_brightness [ positioned ~ ~1 ~ ]
#			iyc:custom_blocks/compute_brightness [ positioned ~ ~-1 ~ ]
#			iyc:custom_blocks/compute_brightness [ positioned ~1 ~ ~ ]
#			iyc:custom_blocks/compute_brightness [ positioned ~-1 ~ ~ ]
#			iyc:custom_blocks/compute_brightness [ positioned ~ ~ ~1 ]
#			iyc:custom_blocks/compute_brightness [ positioned ~ ~ ~-1 ]
#

# Check light level at current position and update #light if higher
execute if score #light iyc.data matches ..0 if predicate iyc:light/1 run return run scoreboard players set #light iyc.data 1
execute if score #light iyc.data matches ..1 if predicate iyc:light/2 run return run scoreboard players set #light iyc.data 2
execute if score #light iyc.data matches ..2 if predicate iyc:light/3 run return run scoreboard players set #light iyc.data 3
execute if score #light iyc.data matches ..3 if predicate iyc:light/4 run return run scoreboard players set #light iyc.data 4
execute if score #light iyc.data matches ..4 if predicate iyc:light/5 run return run scoreboard players set #light iyc.data 5
execute if score #light iyc.data matches ..5 if predicate iyc:light/6 run return run scoreboard players set #light iyc.data 6
execute if score #light iyc.data matches ..6 if predicate iyc:light/7 run return run scoreboard players set #light iyc.data 7
execute if score #light iyc.data matches ..7 if predicate iyc:light/8 run return run scoreboard players set #light iyc.data 8
execute if score #light iyc.data matches ..8 if predicate iyc:light/9 run return run scoreboard players set #light iyc.data 9
execute if score #light iyc.data matches ..9 if predicate iyc:light/10 run return run scoreboard players set #light iyc.data 10
execute if score #light iyc.data matches ..10 if predicate iyc:light/11 run return run scoreboard players set #light iyc.data 11
execute if score #light iyc.data matches ..11 if predicate iyc:light/12 run return run scoreboard players set #light iyc.data 12
execute if score #light iyc.data matches ..12 if predicate iyc:light/13 run return run scoreboard players set #light iyc.data 13
execute if score #light iyc.data matches ..13 if predicate iyc:light/14 run return run scoreboard players set #light iyc.data 14
execute if score #light iyc.data matches ..14 if predicate iyc:light/15 run return run scoreboard players set #light iyc.data 15

