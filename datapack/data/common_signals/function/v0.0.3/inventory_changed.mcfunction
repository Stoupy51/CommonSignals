
advancement revoke @s only common_signals:v0.0.3/inventory_changed
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 3 run function common_signals:v0.0.3/technical/inventory_changed

