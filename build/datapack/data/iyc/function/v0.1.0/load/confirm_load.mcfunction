
#> iyc:v0.1.0/load/confirm_load
#
# @within	iyc:v0.1.0/load/valid_dependencies
#

# Create objectives for growing seeds
scoreboard objectives add iyc.growth_time dummy
scoreboard objectives add iyc.growth_stage dummy

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded ImagineYourCraft v0.1.0]","color":"green"}
scoreboard players set #iyc.loaded load.status 1
function iyc:v0.1.0/load/set_items_storage

scoreboard objectives add iyc.shape dummy

scoreboard objectives add iyc.jump dummy

