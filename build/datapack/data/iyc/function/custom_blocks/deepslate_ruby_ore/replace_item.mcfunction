
#> iyc:custom_blocks/deepslate_ruby_ore/replace_item
#
# @within	iyc:custom_blocks/deepslate_ruby_ore/destroy
#

# If silk touch applied
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.id set from storage iyc:items all.deepslate_ruby_ore.id
execute if score #is_silk_touch iyc.data matches 1 run data modify entity @s Item.components set from storage iyc:items all.deepslate_ruby_ore.components

# Else, no silk touch
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.id set from storage iyc:items all.ruby.id
execute if score #is_silk_touch iyc.data matches 0 run data modify entity @s Item.components set from storage iyc:items all.ruby.components

# Get item count in every case
execute store result entity @s Item.count byte 1 run scoreboard players get #item_count iyc.data

