
#> iyc:shapes/stairs_1/facing_south/half_bottom
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_south
#

execute if block ~ ~ ~ #iyc:hosts/stairs[shape=straight] run return run function iyc:shapes/apply/2
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_right] run return run function iyc:shapes/apply/6
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_left] run return run function iyc:shapes/apply/4
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_right] run return run function iyc:shapes/apply/10
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_left] run return run function iyc:shapes/apply/8

