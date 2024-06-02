
# If current major is too low, set it to the current major
execute unless score #common_signals.major load.status matches 0.. run scoreboard players set #common_signals.major load.status 0

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #common_signals.major load.status matches 0 unless score #common_signals.minor load.status matches 0.. run scoreboard players set #common_signals.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #common_signals.major load.status matches 0 if score #common_signals.minor load.status matches 0 unless score #common_signals.patch load.status matches 0.. run scoreboard players set #common_signals.patch load.status 3

