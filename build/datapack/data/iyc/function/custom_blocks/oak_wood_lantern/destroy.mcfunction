
#> iyc:custom_blocks/oak_wood_lantern/destroy
#
# @within	iyc:custom_blocks/_groups/minecraft_ochre_froglight
#

# Replace the item with the custom one
execute as @e[type=item,nbt={Item:{id:"minecraft:ochre_froglight"}},limit=1,sort=nearest,distance=..1] run function iyc:custom_blocks/oak_wood_lantern/replace_item

# Decrease count scores
scoreboard players remove #total_custom_blocks iyc.data 1
scoreboard players remove #total_vanilla_ochre_froglight iyc.data 1
scoreboard players remove #total_oak_wood_lantern iyc.data 1

# Kill the custom block entity
kill @s

