
#> iyc:interaction/use
#
# @executed	at @s
#
# @within	iyc:interaction/used [ at @s ]
#

data remove entity @s interaction
execute if entity @s[tag=iyc.seat.50] unless entity @p[tag=iyc.user,predicate=iyc:has_vehicle] run return run function iyc:interaction/sit {height:0.5}
execute if entity @s[tag=iyc.seat.59] unless entity @p[tag=iyc.user,predicate=iyc:has_vehicle] run return run function iyc:interaction/sit {height:0.59}
execute if entity @s[tag=iyc.seat.88] unless entity @p[tag=iyc.user,predicate=iyc:has_vehicle] run return run function iyc:interaction/sit {height:0.875}
execute if entity @s[tag=iyc.lights.black_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"black_lit_lamp"}
execute if entity @s[tag=iyc.lights.blue_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"blue_lit_lamp"}
execute if entity @s[tag=iyc.lights.brown_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"brown_lit_lamp"}
execute if entity @s[tag=iyc.lights.cyan_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"cyan_lit_lamp"}
execute if entity @s[tag=iyc.lights.gray_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"gray_lit_lamp"}
execute if entity @s[tag=iyc.lights.green_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"green_lit_lamp"}
execute if entity @s[tag=iyc.lights.light_blue_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"light_blue_lit_lamp"}
execute if entity @s[tag=iyc.lights.light_gray_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"light_gray_lit_lamp"}
execute if entity @s[tag=iyc.lights.lime_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"lime_lit_lamp"}
execute if entity @s[tag=iyc.lights.magenta_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"magenta_lit_lamp"}
execute if entity @s[tag=iyc.lights.orange_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"orange_lit_lamp"}
execute if entity @s[tag=iyc.lights.pink_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"pink_lit_lamp"}
execute if entity @s[tag=iyc.lights.purple_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"purple_lit_lamp"}
execute if entity @s[tag=iyc.lights.red_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"red_lit_lamp"}
execute if entity @s[tag=iyc.lights.white_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"white_lit_lamp"}
execute if entity @s[tag=iyc.lights.yellow_lit_lamp] if items entity @p[tag=iyc.user] weapon.mainhand minecraft:flint_and_steel align xyz positioned ~0.5 ~0.5 ~0.5 run return run function iyc:interaction/light {lit:"yellow_lit_lamp"}

