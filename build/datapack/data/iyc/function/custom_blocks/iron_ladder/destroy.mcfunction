
#> iyc:custom_blocks/iron_ladder/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_ladder
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:ladder"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/iron_ladder/replace_item

# Kill the custom block entity
kill @s

