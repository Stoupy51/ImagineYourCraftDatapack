
#> iyc:custom_blocks/no_block_below
#
# @executed	at @s
#
# @within	iyc:custom_blocks/destroy_growing_seeds {item:"hops_seeds"}
#
# @args		item (string)
#

# Break the block we're at and call the destroy function
execute if entity @s[type=item_frame] run summon item ~ ~ ~ {Item:{id:"minecraft:item_frame",count:1,components:{"minecraft:custom_data":{"iyc":{"item_frame_destroy":true}}}}}
execute if entity @s[type=item_display] run setblock ~ ~ ~ air destroy
$function iyc:custom_blocks/$(item)/destroy

