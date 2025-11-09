
#> common_signals:v0.1.2/technical/on_new_item
#
# @executed	as @e[type=item,tag=!common_signals.checked]
#
# @within	common_signals:v0.1.2/tick [ as @e[type=item,tag=!common_signals.checked] ]
#

tag @s add common_signals.checked
function #common_signals:signals/on_new_item

# Check if the item is a temporary item and kill it
execute if data entity @s Item.components."minecraft:custom_data".common_signals.temp run kill @s

