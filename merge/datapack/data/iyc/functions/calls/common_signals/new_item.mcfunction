
# If the item is not dropped by a player and count < 8, run special function
execute unless data entity @s Thrower unless data entity @s Owner if items entity @s container.0 *[count~{max:8}] run function iyc:calls/common_signals/handle_item

