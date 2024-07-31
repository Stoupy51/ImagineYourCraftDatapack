
#> iyc:custom_blocks/blue_block_ctf/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_glass
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:glass"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/blue_block_ctf/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_glass iyc.data 1
scoreboard players remove #total_blue_block_ctf iyc.data 1

# Kill the custom block entity
kill @s

