
#> iyc:custom_blocks/topaz_ore/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_polished_deepslate
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/topaz_ore/replace_item

# Kill the custom block entity
kill @s

