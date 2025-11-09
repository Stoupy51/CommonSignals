
#> common_signals:v0.2.0/inventory_changed
#
# @executed	as the player & at current position
#
# @within	advancement common_signals:v0.2.0/inventory_changed
#

advancement revoke @s only common_signals:v0.2.0/inventory_changed
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 2 if score #common_signals.patch load.status matches 0 run function common_signals:v0.2.0/technical/inventory_changed

