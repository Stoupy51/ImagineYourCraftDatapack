
#> iyc:shapes/furnace_21/facing_north
#
# @executed	at @s
#
# @within	iyc:shapes/furnace_21
#

execute if block ~ ~ ~ #iyc:hosts/furnace[lit=false] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/furnace[lit=true] run return run function iyc:shapes/apply/1

