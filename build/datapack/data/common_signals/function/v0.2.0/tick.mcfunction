
#> common_signals:v0.2.0/tick
#
# @within	common_signals:v0.2.0/destroyed_block
#			common_signals:v0.2.0/load/tick_verification
#

# For each new item discovered, run a signal
execute as @e[type=item,tag=!common_signals.checked] run function common_signals:v0.2.0/technical/on_new_item

