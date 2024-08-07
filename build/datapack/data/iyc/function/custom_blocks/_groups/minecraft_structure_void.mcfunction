
#> iyc:custom_blocks/_groups/minecraft_structure_void
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_clear_glass iyc.data matches 1.. if entity @s[tag=iyc.clear_glass] run function iyc:custom_blocks/clear_glass/destroy
execute if score #total_cloud iyc.data matches 1.. if entity @s[tag=iyc.cloud] run function iyc:custom_blocks/cloud/destroy
execute if score #total_flatware iyc.data matches 1.. if entity @s[tag=iyc.flatware] run function iyc:custom_blocks/flatware/destroy
execute if score #total_black_flower iyc.data matches 1.. if entity @s[tag=iyc.black_flower] run function iyc:custom_blocks/black_flower/destroy
execute if score #total_blue_flower iyc.data matches 1.. if entity @s[tag=iyc.blue_flower] run function iyc:custom_blocks/blue_flower/destroy
execute if score #total_white_flower iyc.data matches 1.. if entity @s[tag=iyc.white_flower] run function iyc:custom_blocks/white_flower/destroy
execute if score #total_blob iyc.data matches 1.. if entity @s[tag=iyc.blob] run function iyc:custom_blocks/blob/destroy

