
#> iyc:custom_blocks/destroy_growing_seeds
#
# @executed	at @s
#
# @within	iyc:v0.1.0/second_5 [ at @s ]
#

execute if score #total_hops_seeds iyc.data matches 1.. if entity @s[tag=iyc.hops_seeds] unless block ~ ~-1 ~ farmland run return run function iyc:custom_blocks/no_block_below {item:"hops_seeds"}

