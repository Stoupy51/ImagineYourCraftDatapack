
#> iyc:shapes/trapdoor_5/facing_east/half_bottom
#
# @executed	at @s
#
# @within	iyc:shapes/trapdoor_5/facing_east
#

execute if block ~ ~ ~ #iyc:hosts/trapdoor[open=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/trapdoor[open=true] run return run function iyc:shapes/apply/25

