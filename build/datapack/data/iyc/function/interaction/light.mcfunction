
#> iyc:interaction/light
#
# @executed	align xyz & positioned ~0.5 ~0.5 ~0.5
#
# @within	iyc:interaction/use {lit:"black_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"blue_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"brown_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"cyan_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"gray_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"green_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"light_blue_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"light_gray_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"lime_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"magenta_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"orange_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"pink_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"purple_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"red_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"white_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:interaction/use {lit:"yellow_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#
# @args		lit (string)
#

setblock ~ ~ ~ air
execute as @e[type=item_display,tag=iyc.custom_block,distance=..0.1] run function iyc:custom_blocks/destroy
$function iyc:custom_blocks/$(lit)/place_main

