import math

cookies_per_day = int(input())
workers = int(input())
competing_factory_produce = int(input())

total_produce = 0

for day in range(1, 30 + 1):
    if day % 3 == 0:
        total_produce += math.floor((cookies_per_day * workers) * 0.75)
    else:
        total_produce += math.floor(cookies_per_day * workers)

print(f"You have produced {total_produce} biscuits for the past month.")

if total_produce > competing_factory_produce:
    difference = total_produce - competing_factory_produce
    percent_difference = (difference / competing_factory_produce) * 100

    print(f"You produce {percent_difference:.2f} percent more biscuits.")
else:
    difference = abs(total_produce - competing_factory_produce)
    percent_difference = abs(difference / competing_factory_produce) * 100

    print(f"You produce {percent_difference:.2f} percent less biscuits.")


