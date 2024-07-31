
#> iyc:v0.0.1/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #iyc.major load.status matches 0 if score #iyc.minor load.status matches 0 if score #iyc.patch load.status matches 1 run function iyc:v0.0.1/tick

