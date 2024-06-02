
schedule clear common_signals:v0.0.3/technical/tick
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 3 run schedule function common_signals:v0.0.3/technical/tick 1t

