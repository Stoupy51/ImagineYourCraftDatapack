
#> iyc:custom_blocks/ruby_ore/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_polished_deepslate
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:polished_deepslate"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/ruby_ore/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_polished_deepslate iyc.data 1
scoreboard players remove #total_ruby_ore iyc.data 1

# Kill the custom block entity
kill @s

