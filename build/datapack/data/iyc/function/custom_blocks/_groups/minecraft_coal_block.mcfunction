
#> iyc:custom_blocks/_groups/minecraft_coal_block
#
# @within	iyc:custom_blocks/destroy
#

execute if entity @s[tag=iyc.lignite_block] run function iyc:custom_blocks/lignite_block/destroy
execute if entity @s[tag=iyc.slate_block] run function iyc:custom_blocks/slate_block/destroy

