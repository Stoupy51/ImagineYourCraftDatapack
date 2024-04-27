
# Copy Owner UUID
data modify entity @s data.Owner set from storage imagineyourcraft:main Owner

# Mount the snowball to track position
ride @s mount @e[type=snowball,tag=imagineyourcraft.temp,limit=1]

# Increment markers score to enable marker ticking
scoreboard players add #rock_markers imagineyourcraft.data 1

# Add tag for identification
tag @s add imagineyourcraft.rock_marker
tag @s add smithed.strict

