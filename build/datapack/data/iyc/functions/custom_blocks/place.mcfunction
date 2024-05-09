
#> iyc:custom_blocks/place
#
# @within	iyc:custom_blocks/on_place
#

tag @s add iyc.placer
execute if data storage smithed.custom_block:main blockApi{id:"iyc:adamantium_block"} run function iyc:custom_blocks/adamantium_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:adamantium_ore"} run function iyc:custom_blocks/adamantium_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:sapphire_block"} run function iyc:custom_blocks/sapphire_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:sapphire_ore"} run function iyc:custom_blocks/sapphire_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:ruby_block"} run function iyc:custom_blocks/ruby_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:ruby_ore"} run function iyc:custom_blocks/ruby_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:topaz_block"} run function iyc:custom_blocks/topaz_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:topaz_ore"} run function iyc:custom_blocks/topaz_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:massive_obsidian_block"} run function iyc:custom_blocks/massive_obsidian_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:steel_block"} run function iyc:custom_blocks/steel_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:steel_ore"} run function iyc:custom_blocks/steel_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:lignite_block"} run function iyc:custom_blocks/lignite_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:lignite_ore"} run function iyc:custom_blocks/lignite_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:slate_block"} run function iyc:custom_blocks/slate_block/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:slate_ore"} run function iyc:custom_blocks/slate_ore/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:iron_furnace"} run function iyc:custom_blocks/iron_furnace/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:box_jump"} run function iyc:custom_blocks/box_jump/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:box_speed"} run function iyc:custom_blocks/box_speed/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:blue_block_ctf"} run function iyc:custom_blocks/blue_block_ctf/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:clear_glass"} run function iyc:custom_blocks/clear_glass/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:birch_wood_lantern"} run function iyc:custom_blocks/birch_wood_lantern/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:jungle_wood_lantern"} run function iyc:custom_blocks/jungle_wood_lantern/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:oak_wood_lantern"} run function iyc:custom_blocks/oak_wood_lantern/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:spruce_wood_lantern"} run function iyc:custom_blocks/spruce_wood_lantern/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:iron_lantern"} run function iyc:custom_blocks/iron_lantern/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:red_light"} run function iyc:custom_blocks/red_light/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:reversed_oak_planks"} run function iyc:custom_blocks/reversed_oak_planks/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:cherry_cake"} run function iyc:custom_blocks/cherry_cake/place_main
execute if data storage smithed.custom_block:main blockApi{id:"iyc:nuclear_bomb"} run function iyc:custom_blocks/nuclear_bomb/place_main
tag @s remove iyc.placer

