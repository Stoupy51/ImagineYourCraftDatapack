
#> iyc:custom_blocks/lignite_torch/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_torch
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:torch"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/lignite_torch/replace_item

# Kill the custom block entity
kill @s

