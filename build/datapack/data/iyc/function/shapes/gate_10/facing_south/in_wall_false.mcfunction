
#> iyc:shapes/gate_10/facing_south/in_wall_false
#
# @executed	at @s
#
# @within	iyc:shapes/gate_10/facing_south
#

execute if block ~ ~ ~ #iyc:hosts/gate[open=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/gate[open=true] run return run function iyc:shapes/apply/4

