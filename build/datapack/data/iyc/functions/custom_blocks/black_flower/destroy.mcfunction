
#> iyc:custom_blocks/black_flower/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_structure_void
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:structure_void"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/black_flower/replace_item

# Kill the custom block entity
kill @s

