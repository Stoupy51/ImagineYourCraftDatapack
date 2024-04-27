
# If the item is sugar cane, 10% chance of replacing to taurine
execute if items entity @s container.0 sugar_cane if predicate {condition:random_chance,chance:0.1} run data modify entity @s Item set from storage iyc:items all.taurine

# If the item is hops, 10% chance of replacing to caffeine
execute if items entity @s container.0 *[custom_data~{iyc:{hops:1b}}] if predicate {condition:random_chance,chance:0.1} run data modify entity @s Item set from storage iyc:items all.caffeine

# If the item is wheat, 10% chance of replacing to cola
execute if items entity @s container.0 wheat if predicate {condition:random_chance,chance:0.1} run data modify entity @s Item set from storage iyc:items all.cola

# If the item is cobblestone, 5% chance of replacing to rock
execute if items entity @s container.0 cobblestone if predicate {condition:random_chance,chance:0.05} run data modify entity @s Item set from storage iyc:items all.rock

