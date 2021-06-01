WATER_TANK = 255

attempts = int(input())

capacity = 0

for attempt in range(attempts):
    current_litres = int(input())
    capacity += current_litres
    if capacity > WATER_TANK:
        print("Insufficient capacity!")
        capacity -= current_litres
        continue

print(capacity)