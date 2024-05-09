
#> iyc:custom_blocks/red_light/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_red_concrete
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:red_concrete"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/red_light/replace_item

# Kill the custom block entity
kill @s

