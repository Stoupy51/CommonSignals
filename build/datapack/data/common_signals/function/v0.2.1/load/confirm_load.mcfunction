
#> common_signals:v0.2.1/load/confirm_load
#
# @within	common_signals:v0.2.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded Common Signals v0.2.1]","color":"green"}
scoreboard players set #common_signals.loaded load.status 1
function common_signals:v0.2.1/load/set_items_storage

