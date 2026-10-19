
#> iyc:custom_blocks/hops_seeds/update_seed_model
#
# @executed	at @s
#
# @within	iyc:custom_blocks/hops_seeds/place_secondary
#			iyc:custom_blocks/hops_seeds/minute
#

# Update growth stage based on growth_time
execute if score @s iyc.growth_time matches 0..67 unless score @s iyc.growth_stage matches 0 run function iyc:custom_blocks/change_seed_stage {stage:0, model:"iyc:seeds/hops_stage_0"}
execute if score @s iyc.growth_time matches 68..136 unless score @s iyc.growth_stage matches 1 run function iyc:custom_blocks/change_seed_stage {stage:1, model:"iyc:seeds/hops_stage_1"}
execute if score @s iyc.growth_time matches 137..204 unless score @s iyc.growth_stage matches 2 run function iyc:custom_blocks/change_seed_stage {stage:2, model:"iyc:seeds/hops_stage_2"}
execute if score @s iyc.growth_time matches 205..273 unless score @s iyc.growth_stage matches 3 run function iyc:custom_blocks/change_seed_stage {stage:3, model:"iyc:seeds/hops_stage_3"}
execute if score @s iyc.growth_time matches 274..341 unless score @s iyc.growth_stage matches 4 run function iyc:custom_blocks/change_seed_stage {stage:4, model:"iyc:seeds/hops_stage_4"}
execute if score @s iyc.growth_time matches 342..410 unless score @s iyc.growth_stage matches 5 run function iyc:custom_blocks/change_seed_stage {stage:5, model:"iyc:seeds/hops_stage_5"}
execute if score @s iyc.growth_time matches 411..479 unless score @s iyc.growth_stage matches 6 run function iyc:custom_blocks/change_seed_stage {stage:6, model:"iyc:seeds/hops_stage_6"}
execute if score @s iyc.growth_time matches 480.. unless score @s iyc.growth_stage matches 7 run function iyc:custom_blocks/change_seed_stage {stage:7, model:"iyc:seeds/hops_stage_7"}

