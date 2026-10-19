
#> iyc:shapes/gate_10/facing_east/in_wall_false
#
# @executed	at @s
#
# @within	iyc:shapes/gate_10/facing_east
#

execute if block ~ ~ ~ #iyc:hosts/gate[open=false] run return run function iyc:shapes/apply/3
execute if block ~ ~ ~ #iyc:hosts/gate[open=true] run return run function iyc:shapes/apply/7

