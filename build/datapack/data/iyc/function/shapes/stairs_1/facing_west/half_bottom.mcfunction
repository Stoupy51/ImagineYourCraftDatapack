
#> iyc:shapes/stairs_1/facing_west/half_bottom
#
# @executed	at @s
#
# @within	iyc:shapes/stairs_1/facing_west
#

execute if block ~ ~ ~ #iyc:hosts/stairs[shape=straight] run return run function iyc:shapes/apply/1
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_right] run return run function iyc:shapes/apply/5
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=outer_left] run return run function iyc:shapes/apply/6
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_right] run return run function iyc:shapes/apply/9
execute if block ~ ~ ~ #iyc:hosts/stairs[shape=inner_left] run return run function iyc:shapes/apply/10

