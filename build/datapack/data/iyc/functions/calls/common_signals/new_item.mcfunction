
#> iyc:calls/common_signals/new_item
#
# @within	#common_signals:signals/on_new_item
#

# If the item is from a custom ore, launch the on_ore_destroyed function
execute if data entity @s Item.components."minecraft:custom_data".common_signals.temp at @s align xyz run function iyc:calls/common_signals/on_ore_destroyed

# If the item is not dropped by a player and count <= 8, run special function
execute unless data entity @s Thrower unless data entity @s Owner if items entity @s container.0 *[count~{max:8}] run function iyc:calls/common_signals/handle_item

