
# Copy Owner UUID
data modify entity @s data.Owner set from storage iyc:main Owner

# Mount the snowball to track position
ride @s mount @e[type=snowball,tag=iyc.temp,limit=1]

# Increment markers score to enable marker ticking
scoreboard players add #rock_markers iyc.data 1

# Add tag for identification
tag @s add iyc.rock_marker
tag @s add smithed.strict

