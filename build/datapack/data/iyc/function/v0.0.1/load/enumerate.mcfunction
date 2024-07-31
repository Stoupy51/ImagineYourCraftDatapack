
#> iyc:v0.0.1/load/enumerate
#
# @within	#iyc:enumerate
#

# If current major is too low, set it to the current major
execute unless score #iyc.major load.status matches 0.. run scoreboard players set #iyc.major load.status 0

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #iyc.major load.status matches 0 unless score #iyc.minor load.status matches 0.. run scoreboard players set #iyc.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #iyc.major load.status matches 0 if score #iyc.minor load.status matches 0 unless score #iyc.patch load.status matches 1.. run scoreboard players set #iyc.patch load.status 1

