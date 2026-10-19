
#> iyc:shapes/gate_10/facing_south
#
# @executed	at @s
#
# @within	iyc:shapes/gate_10
#

execute if block ~ ~ ~ #iyc:hosts/gate[in_wall=false] run return run function iyc:shapes/gate_10/facing_south/in_wall_false
execute if block ~ ~ ~ #iyc:hosts/gate[in_wall=true] run return run function iyc:shapes/gate_10/facing_south/in_wall_true

