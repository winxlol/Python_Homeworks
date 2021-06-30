def attack(ship, row, coloum):
    destroyed_ships = 0
    if ship[row][coloum] > 0:
        ship[row][coloum] -= 1
        if ship[row][coloum] == 0:
            destroyed_ships += 1
            return destroyed_ships
        else:
            return ship


rows = int(input())

ship = []
destroyed_targets = 0

for row in range(rows):
    current_row = input().split()

    current_row = [int(el) for el in current_row]
    ship.append(current_row)

attack_information = input().split()

for current_attack in range(len(attack_information)):
    attack_coordinates = attack_information[current_attack].split("-")

    row = int(attack_coordinates[0])
    coloum = int(attack_coordinates[1])

    current_target = attack(ship, row, coloum)
    if current_target == 1:
        destroyed_targets += current_target


print(destroyed_targets)
