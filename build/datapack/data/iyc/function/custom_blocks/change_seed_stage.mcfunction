
#> iyc:custom_blocks/change_seed_stage
#
# @executed	at @s
#
# @within	iyc:custom_blocks/hops_seeds/update_seed_model {stage:0, model:"iyc:seeds/hops_stage_0"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:1, model:"iyc:seeds/hops_stage_1"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:2, model:"iyc:seeds/hops_stage_2"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:3, model:"iyc:seeds/hops_stage_3"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:4, model:"iyc:seeds/hops_stage_4"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:5, model:"iyc:seeds/hops_stage_5"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:6, model:"iyc:seeds/hops_stage_6"}
#			iyc:custom_blocks/hops_seeds/update_seed_model {stage:7, model:"iyc:seeds/hops_stage_7"}
#
# @args		stage (int)
#			model (string)
#

# Update the growth stage score
$scoreboard players set @s iyc.growth_stage $(stage)

# Change the item model to the right stage
$execute if entity @s[type=item_display] run return run data modify entity @s item.components."minecraft:item_model" set value "$(model)"
$execute if entity @s[type=item_frame] run return run data modify entity @s Item.components."minecraft:item_model" set value "$(model)"

