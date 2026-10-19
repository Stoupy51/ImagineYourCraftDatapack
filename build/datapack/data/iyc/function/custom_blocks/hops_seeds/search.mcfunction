
#> iyc:custom_blocks/hops_seeds/search
#
# @executed	as the player & at current position
#
# @within	advancement iyc:custom_block_alternative/hops_seeds
#

# Advancement revoke
advancement revoke @s only iyc:custom_block_alternative/hops_seeds

# Execute the place function as and at the new placed item frame
tag @s add iyc.to_refund
execute as @e[type=item_frame,tag=iyc.new,tag=iyc.hops_seeds] at @s run function iyc:custom_blocks/hops_seeds/place_check
tag @s remove iyc.to_refund

