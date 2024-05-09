
#> iyc:load/main
#
# @within	#iyc:load/main
#

# Avoiding multiple executions of the same load function
execute unless score ImagineYourCraft load.status matches 1.. run function iyc:load/secondary

