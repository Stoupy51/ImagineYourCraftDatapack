
#> iyc:interaction/light
#
# @executed	align xyz & positioned ~0.5 ~0.5 ~0.5
#
# @within	iyc:custom_blocks/_interaction/use {lit:"white_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"orange_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"magenta_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"light_blue_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"yellow_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"lime_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"pink_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"gray_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"light_gray_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"cyan_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"purple_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"blue_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"brown_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"green_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"red_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#			iyc:custom_blocks/_interaction/use {lit:"black_lit_lamp"} [ align xyz & positioned ~0.5 ~0.5 ~0.5 ]
#
# @args		lit (string)
#

scoreboard players set #no_drop iyc.data 1
function iyc:custom_blocks/_interaction/break
$function iyc:custom_blocks/$(lit)/place_main

