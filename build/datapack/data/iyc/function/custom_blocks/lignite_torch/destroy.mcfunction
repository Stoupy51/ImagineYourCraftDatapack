
#> iyc:custom_blocks/lignite_torch/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_torch
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:torch"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/lignite_torch/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_torch iyc.data 1
scoreboard players remove #total_lignite_torch iyc.data 1

# Kill the custom block entity
kill @s

