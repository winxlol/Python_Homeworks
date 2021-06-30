neighborhood = input().split("@")
neighborhood = [int(el) for el in neighborhood]

house_index = 0
last_position = None

while True:
    tokens = input()

    if tokens == "Love!":
        break

    jump = tokens.split()
    jump_length = int(jump[1])

    house_index += jump_length
    last_position = house_index

    if house_index >= len(neighborhood):
        house_index = 0

        last_position = house_index
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
            continue

        neighborhood[house_index] -= 2

        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")

    else:
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
            continue

        neighborhood[house_index] -= 2

        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")


valentine_houses = [el for el in neighborhood if el == 0]
none_valentine_houses = [el for el in neighborhood if not el == 0]

print(f"Cupid's last position was {last_position}.")

if len(valentine_houses) == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(none_valentine_houses)} places.")
