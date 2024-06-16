
#> common_signals:v0.0.4/inventory_changed
#
# @within	advancement common_signals:v0.0.4/inventory_changed
#

advancement revoke @s only common_signals:v0.0.4/inventory_changed
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 4 run function common_signals:v0.0.4/technical/inventory_changed

