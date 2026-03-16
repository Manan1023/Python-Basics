day1_visitors = {101,102,103,104,105}
day2_visitors = {104,105,106,107,108}

both_days = day1_visitors.intersection(day2_visitors)

only_one_day = day1_visitors.symmetric_difference(day2_visitors)

total_unique = day1_visitors.union(day2_visitors)

print(f"Visited both days: {both_days}")
print(f"Visited only one day:{only_one_day}")
print(f"Total unique visitors :{total_unique}")
