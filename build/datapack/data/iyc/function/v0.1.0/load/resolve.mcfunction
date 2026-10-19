
#> iyc:v0.1.0/load/resolve
#
# @within	#iyc:resolve
#

# If correct version, load the datapack
execute if score #iyc.major load.status matches 0 if score #iyc.minor load.status matches 1 if score #iyc.patch load.status matches 0 run function iyc:v0.1.0/load/main

