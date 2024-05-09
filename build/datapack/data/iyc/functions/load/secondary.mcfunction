
#> iyc:load/secondary
#
# @within	iyc:load/main
#

# ImagineYourCraft
scoreboard objectives add iyc.data dummy
scoreboard players set #iyc.major load.status 0
scoreboard players set #iyc.minor load.status 0
scoreboard players set #iyc.patch load.status 1
tag Stoupy51 add convention.debug


# Check dependencies and wait for a player to connect (to get server version)
function iyc:load/check_dependencies
function iyc:load/waiting_for_player

