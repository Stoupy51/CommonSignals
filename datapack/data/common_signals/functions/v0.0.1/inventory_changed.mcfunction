
advancement revoke @s only common_signals:v0.0.1/inventory_changed
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 1 run function common_signals:v0.0.1/technical/inventory_changed

