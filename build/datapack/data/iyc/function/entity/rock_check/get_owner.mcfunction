
#> iyc:entity/rock_check/get_owner
#
# @within	iyc:entity/rock_check/marker_final
#

# Stop if already found
execute if score #success iyc.data matches 0 run return 0

# Compare UUIDs and tag the player if same
data modify storage iyc:main copy set from storage iyc:main Owner
execute store success score #success iyc.data run data modify storage iyc:main copy set from entity @s UUID
execute if score #success iyc.data matches 0 run tag @s add iyc.owner
execute if score #success iyc.data matches 0 run return 1

