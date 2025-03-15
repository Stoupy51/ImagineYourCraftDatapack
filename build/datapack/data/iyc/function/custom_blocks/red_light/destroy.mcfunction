
#> iyc:custom_blocks/red_light/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_red_concrete
#

# Replace the item with the custom one
execute as @n[type=item,nbt={Item:{id:"minecraft:red_concrete"}},distance=..1] run function iyc:custom_blocks/red_light/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_red_concrete iyc.data 1
scoreboard players remove #total_red_light iyc.data 1

# Kill the custom block entity
kill @s

