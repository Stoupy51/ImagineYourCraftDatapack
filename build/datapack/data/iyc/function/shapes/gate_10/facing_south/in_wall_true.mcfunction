
#> iyc:shapes/gate_10/facing_south/in_wall_true
#
# @executed	at @s
#
# @within	iyc:shapes/gate_10/facing_south
#

execute if block ~ ~ ~ #iyc:hosts/gate[open=false] run return run function iyc:shapes/apply/8
execute if block ~ ~ ~ #iyc:hosts/gate[open=true] run return run function iyc:shapes/apply/12

