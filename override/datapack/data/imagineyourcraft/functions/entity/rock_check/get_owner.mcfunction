
# Stop if already found
execute if score #success imagineyourcraft.data matches 0 run return 0

# Compare UUIDs and tag the player if same
data modify storage imagineyourcraft:main copy set from storage imagineyourcraft:main Owner
execute store success score #success imagineyourcraft.data run data modify storage imagineyourcraft:main copy set from entity @s UUID
execute if score #success imagineyourcraft.data matches 0 run tag @s add imagineyourcraft.owner
execute if score #success imagineyourcraft.data matches 0 run return 1

