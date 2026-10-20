
#> iyc:custom_blocks/_interaction/use
#
# @executed	at @s
#
# @within	iyc:custom_blocks/_interaction/used [ at @s ]
#

data remove entity @s interaction
execute if entity @s[tag=iyc.oak_stool] run return run function iyc:custom_blocks/oak_stool/sit
execute if entity @s[tag=iyc.birch_stool] run return run function iyc:custom_blocks/birch_stool/sit
execute if entity @s[tag=iyc.cobblestone_stool] run return run function iyc:custom_blocks/cobblestone_stool/sit
execute if entity @s[tag=iyc.stone_stool] run return run function iyc:custom_blocks/stone_stool/sit
execute if entity @s[tag=iyc.oak_high_stool] run return run function iyc:custom_blocks/oak_high_stool/sit
execute if entity @s[tag=iyc.birch_high_stool] run return run function iyc:custom_blocks/birch_high_stool/sit
execute if entity @s[tag=iyc.cobblestone_high_stool] run return run function iyc:custom_blocks/cobblestone_high_stool/sit
execute if entity @s[tag=iyc.stone_high_stool] run return run function iyc:custom_blocks/stone_high_stool/sit
execute if entity @s[tag=iyc.oak_bench] run return run function iyc:custom_blocks/oak_bench/sit
execute if entity @s[tag=iyc.birch_bench] run return run function iyc:custom_blocks/birch_bench/sit
execute if entity @s[tag=iyc.cobblestone_bench] run return run function iyc:custom_blocks/cobblestone_bench/sit
execute if entity @s[tag=iyc.stone_bench] run return run function iyc:custom_blocks/stone_bench/sit
execute if entity @s[tag=iyc.oak_chair] run return run function iyc:custom_blocks/oak_chair/sit
execute if entity @s[tag=iyc.birch_chair] run return run function iyc:custom_blocks/birch_chair/sit
execute if entity @s[tag=iyc.cobblestone_chair] run return run function iyc:custom_blocks/cobblestone_chair/sit
execute if entity @s[tag=iyc.stone_chair] run return run function iyc:custom_blocks/stone_chair/sit

execute if entity @s[tag=iyc.white_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"white_lit_lamp"}
execute if entity @s[tag=iyc.orange_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"orange_lit_lamp"}
execute if entity @s[tag=iyc.magenta_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"magenta_lit_lamp"}
execute if entity @s[tag=iyc.light_blue_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"light_blue_lit_lamp"}
execute if entity @s[tag=iyc.yellow_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"yellow_lit_lamp"}
execute if entity @s[tag=iyc.lime_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"lime_lit_lamp"}
execute if entity @s[tag=iyc.pink_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"pink_lit_lamp"}
execute if entity @s[tag=iyc.gray_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"gray_lit_lamp"}
execute if entity @s[tag=iyc.light_gray_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"light_gray_lit_lamp"}
execute if entity @s[tag=iyc.cyan_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"cyan_lit_lamp"}
execute if entity @s[tag=iyc.purple_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"purple_lit_lamp"}
execute if entity @s[tag=iyc.blue_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"blue_lit_lamp"}
execute if entity @s[tag=iyc.brown_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"brown_lit_lamp"}
execute if entity @s[tag=iyc.green_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"green_lit_lamp"}
execute if entity @s[tag=iyc.red_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"red_lit_lamp"}
execute if entity @s[tag=iyc.black_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"black_lit_lamp"}

