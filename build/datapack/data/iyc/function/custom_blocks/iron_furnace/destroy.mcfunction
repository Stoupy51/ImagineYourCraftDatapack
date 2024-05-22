
#> iyc:custom_blocks/iron_furnace/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_furnace
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:furnace"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/iron_furnace/replace_item

# Kill the custom block entity
kill @s

