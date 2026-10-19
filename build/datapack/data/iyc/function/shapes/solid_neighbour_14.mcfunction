
#> iyc:shapes/solid_neighbour_14
#
# @executed	at @s
#
# @within	iyc:custom_blocks/white_rod/place_secondary
#			iyc:custom_blocks/white_lamp/place_secondary
#			iyc:custom_blocks/white_lit_lamp/place_secondary
#			iyc:custom_blocks/orange_rod/place_secondary
#			iyc:custom_blocks/orange_lamp/place_secondary
#			iyc:custom_blocks/orange_lit_lamp/place_secondary
#			iyc:custom_blocks/magenta_rod/place_secondary
#			iyc:custom_blocks/magenta_lamp/place_secondary
#			iyc:custom_blocks/magenta_lit_lamp/place_secondary
#			iyc:custom_blocks/light_blue_rod/place_secondary
#			iyc:custom_blocks/light_blue_lamp/place_secondary
#			iyc:custom_blocks/light_blue_lit_lamp/place_secondary
#			iyc:custom_blocks/yellow_rod/place_secondary
#			iyc:custom_blocks/yellow_lamp/place_secondary
#			iyc:custom_blocks/yellow_lit_lamp/place_secondary
#			iyc:custom_blocks/lime_rod/place_secondary
#			iyc:custom_blocks/lime_lamp/place_secondary
#			iyc:custom_blocks/lime_lit_lamp/place_secondary
#			iyc:custom_blocks/pink_rod/place_secondary
#			iyc:custom_blocks/pink_lamp/place_secondary
#			iyc:custom_blocks/pink_lit_lamp/place_secondary
#			iyc:custom_blocks/gray_rod/place_secondary
#			iyc:custom_blocks/gray_lamp/place_secondary
#			iyc:custom_blocks/gray_lit_lamp/place_secondary
#			iyc:custom_blocks/light_gray_rod/place_secondary
#			iyc:custom_blocks/light_gray_lamp/place_secondary
#			iyc:custom_blocks/light_gray_lit_lamp/place_secondary
#			iyc:custom_blocks/cyan_rod/place_secondary
#			iyc:custom_blocks/cyan_lamp/place_secondary
#			iyc:custom_blocks/cyan_lit_lamp/place_secondary
#			iyc:custom_blocks/purple_rod/place_secondary
#			iyc:custom_blocks/purple_lamp/place_secondary
#			iyc:custom_blocks/purple_lit_lamp/place_secondary
#			iyc:custom_blocks/blue_rod/place_secondary
#			iyc:custom_blocks/blue_lamp/place_secondary
#			iyc:custom_blocks/blue_lit_lamp/place_secondary
#			iyc:custom_blocks/brown_rod/place_secondary
#			iyc:custom_blocks/brown_lamp/place_secondary
#			iyc:custom_blocks/brown_lit_lamp/place_secondary
#			iyc:custom_blocks/green_rod/place_secondary
#			iyc:custom_blocks/green_lamp/place_secondary
#			iyc:custom_blocks/green_lit_lamp/place_secondary
#			iyc:custom_blocks/red_rod/place_secondary
#			iyc:custom_blocks/red_lamp/place_secondary
#			iyc:custom_blocks/red_lit_lamp/place_secondary
#			iyc:custom_blocks/black_rod/place_secondary
#			iyc:custom_blocks/black_lamp/place_secondary
#			iyc:custom_blocks/black_lit_lamp/place_secondary
#			iyc:shapes/follow
#

execute store success score #side_bottom iyc.data unless block ~0 ~-1 ~0 #iyc:not_connectable
execute store success score #side_east iyc.data unless block ~1 ~0 ~0 #iyc:not_connectable
execute store success score #side_north iyc.data unless block ~0 ~0 ~-1 #iyc:not_connectable
execute store success score #side_south iyc.data unless block ~0 ~0 ~1 #iyc:not_connectable
execute store success score #side_top iyc.data unless block ~0 ~1 ~0 #iyc:not_connectable
execute store success score #side_west iyc.data unless block ~-1 ~0 ~0 #iyc:not_connectable
execute if score #side_bottom iyc.data matches 0 run return run function iyc:shapes/solid_neighbour_14/bottom_false
execute if score #side_bottom iyc.data matches 1 run return run function iyc:shapes/solid_neighbour_14/bottom_true

