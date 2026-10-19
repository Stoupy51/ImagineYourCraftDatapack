
#> iyc:shapes/gate_10/facing_west/in_wall_false
#
# @executed	at @s
#
# @within	iyc:shapes/gate_10/facing_west
#

execute if block ~ ~ ~ #iyc:hosts/gate[open=false] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/gate[open=true] run return run function iyc:shapes/apply/5

