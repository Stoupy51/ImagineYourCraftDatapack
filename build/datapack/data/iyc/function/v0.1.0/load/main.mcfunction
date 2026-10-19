
#> iyc:v0.1.0/load/main
#
# @within	iyc:v0.1.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #iyc.loaded load.status matches 1 run function iyc:v0.1.0/load/secondary

