
# Add tag to prevent function from running again
tag @s add iyc.bolt_checked

# Stop function if not bolt
execute unless items entity @s container.0 *[custom_data~{iyc:{bolt:1b}}] run return 0

# Multiple damage by 1.5x
execute store result entity @s damage double 0.001 run data get entity @s damage 1500

