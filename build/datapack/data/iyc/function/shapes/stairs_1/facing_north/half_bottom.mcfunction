
#> iyc:shapes/stairs_1/facing_north/half_bottom
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_north
#

execute if block ~ ~ ~ #iyc:hosts/stairs[shape=straight] run return run function iyc:shapes/apply/3
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_right] run return run function iyc:shapes/apply/7
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_left] run return run function iyc:shapes/apply/5
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_right] run return run function iyc:shapes/apply/11
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_left] run return run function iyc:shapes/apply/9

