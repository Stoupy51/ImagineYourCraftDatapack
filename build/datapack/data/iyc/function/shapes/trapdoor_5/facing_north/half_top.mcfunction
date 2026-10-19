
#> iyc:shapes/trapdoor_5/facing_north/half_top
#
# @executed	at @s
#
# @within	iyc:shapes/trapdoor_5/facing_north
#

execute if block ~ ~ ~ #iyc:hosts/trapdoor[open=false] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/trapdoor[open=true] run return run function iyc:shapes/apply/2

