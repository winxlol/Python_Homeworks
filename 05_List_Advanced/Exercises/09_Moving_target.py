def shoot_target(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add_target(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_target(targets, index, radius):
    left_index = index - radius
    right_index = index + radius

    if 0 <= left_index < index < right_index <= len(targets):
        del targets[left_index:right_index + 1]
    else:
        print("Strike missed!")


targets_health = input().split()

targets_health = [int(el) for el in targets_health]

while True:
    commands = input()

    if commands == "End":
        break

    tokens = commands.split()
    type_command = tokens[0]

    if type_command == "Shoot":
        index = int(tokens[1])
        power = int(tokens[2])

        shoot_target(targets_health, index, power)
    elif type_command == "Add":
        index = int(tokens[1])
        value = int(tokens[2])

        add_target(targets_health, index, value)
    elif type_command == "Strike":
        index = int(tokens[1])
        radius = int(tokens[2])

        strike_target(targets_health, index, radius)


parse_to_str = [str(el) for el in targets_health]

print("|".join(parse_to_str))