import math

party_size = int(input())
days_adventure = int(input())

coins = 0
is_third_day = False

for day in range(1, days_adventure + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins += 50
    coins -= party_size * 2

    if day % 3 == 0:
        coins -= party_size * 3
        is_third_day = True
    if day % 5 == 0:
        coins += party_size * 20
        if is_third_day:
            coins -= party_size * 2

    is_third_day = False

coins_per_person = coins / party_size
print(f"{party_size} companions received {math.floor(coins_per_person)} coins each.")
