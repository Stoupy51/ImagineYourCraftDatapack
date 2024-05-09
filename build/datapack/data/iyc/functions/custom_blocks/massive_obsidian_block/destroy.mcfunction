
#> iyc:custom_blocks/massive_obsidian_block/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_netherite_block
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:netherite_block"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/massive_obsidian_block/replace_item

# Kill the custom block entity
kill @s

