
#> iyc:custom_blocks/_groups/minecraft_torch
#
# @within	iyc:custom_blocks/destroy
#

execute if score #total_lignite_torch iyc.data matches 1.. if entity @s[tag=iyc.lignite_torch] run function iyc:custom_blocks/lignite_torch/destroy

