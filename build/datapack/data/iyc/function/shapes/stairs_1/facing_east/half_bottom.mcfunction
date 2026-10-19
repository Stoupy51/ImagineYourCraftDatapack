
#> iyc:shapes/stairs_1/facing_east/half_bottom
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_east
#

execute if block ~ ~ ~ #iyc:hosts/stairs[shape=straight] run return run function iyc:shapes/apply/0
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_right] run return run function iyc:shapes/apply/4
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_left] run return run function iyc:shapes/apply/7
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_right] run return run function iyc:shapes/apply/8
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_left] run return run function iyc:shapes/apply/11

