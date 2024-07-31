
#> iyc:custom_blocks/lignite_block/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_coal_block
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:coal_block"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/lignite_block/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_coal_block iyc.data 1
scoreboard players remove #total_lignite_block iyc.data 1

# Kill the custom block entity
kill @s

