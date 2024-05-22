
#> iyc:custom_blocks/blue_block_ctf/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_glass
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:glass"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/blue_block_ctf/replace_item

# Kill the custom block entity
kill @s

