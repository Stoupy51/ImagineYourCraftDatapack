
#> iyc:custom_blocks/_groups/minecraft_ochre_froglight
#
# @executed	as @e[type=item_display,tag=iyc.custom_block,distance=..0.1]
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_oak_wood_lantern iyc.data matches 1.. if entity @s[tag=iyc.oak_wood_lantern] run function iyc:custom_blocks/oak_wood_lantern/destroy
execute if score #total_spruce_wood_lantern iyc.data matches 1.. if entity @s[tag=iyc.spruce_wood_lantern] run function iyc:custom_blocks/spruce_wood_lantern/destroy
execute if score #total_birch_wood_lantern iyc.data matches 1.. if entity @s[tag=iyc.birch_wood_lantern] run function iyc:custom_blocks/birch_wood_lantern/destroy
execute if score #total_jungle_wood_lantern iyc.data matches 1.. if entity @s[tag=iyc.jungle_wood_lantern] run function iyc:custom_blocks/jungle_wood_lantern/destroy
execute if score #total_iron_lantern iyc.data matches 1.. if entity @s[tag=iyc.iron_lantern] run function iyc:custom_blocks/iron_lantern/destroy
execute if score #total_redstone_lamp_always iyc.data matches 1.. if entity @s[tag=iyc.redstone_lamp_always] run function iyc:custom_blocks/redstone_lamp_always/destroy

