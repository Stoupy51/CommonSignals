
tag @s add common_signals.checked
function #common_signals:signals/on_new_item

# Check if the item is a temporary item and kill it
execute if data entity @s Item.components."minecraft:custom_data".common_signals.temp run kill @s

