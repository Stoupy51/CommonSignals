
# For each new item discovered, run a signal
execute as @e[type=item,tag=!common_signals.checked] run function common_signals:v0.0.1/technical/on_new_item

# Continue ticking
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 if score #common_signals.patch load.status matches 1 run schedule function common_signals:v0.0.1/technical/tick 1t

