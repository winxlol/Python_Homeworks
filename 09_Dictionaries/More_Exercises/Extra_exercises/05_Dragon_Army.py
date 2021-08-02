from collections import defaultdict
numbers = int(input())

dragons = {}
total_points_for_type = {}

for num in range(numbers):
    data = input().split()

    type = data[0]
    name = data[1]
    damage = data[2]
    health = data[3]
    armor = data[4]

    if damage == "null":
        damage = 45
    else:
        damage = int(data[2])
    if health == "null":
        health = 250
    else:
        health = int(data[3])
    if armor == "null":
        armor = 10
    else:
        armor = int(data[4])

    if type not in dragons:
        dragons[type] = {}

    if name not in dragons[type]:
        dragons[type][name] = [damage, health, armor]
    else:
        dragons[type][name] = [damage, health, armor]

    if type not in total_points_for_type:
        total_points_for_type[type] = [damage, health, armor]
    else:
        total_points_for_type[type][0] += damage
        total_points_for_type[type][1] += health
        total_points_for_type[type][2] += armor


for dragon_type, dragon_details in total_points_for_type.items():
    current_dragon = []
    for index in range(len(dragon_details)):
        current_dragon.append(dragon_details[index] / len(dragons[dragon_type]))
    print(f"{dragon_type}::({current_dragon[0]:.2f}/{current_dragon[1]:.2f}/{current_dragon[2]:.2f})")

    for dragon_name, details in sorted(dragons[dragon_type].items(), key=lambda x: x[0]):
        print(f"-{dragon_name} -> damage: {details[0]}, health: {details[1]}, armor: {details[2]}")





















