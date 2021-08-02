def check_type_of_input(data):
    if "|" in data:
        force_side, force_user = data.split(" | ")

        if force_side not in sides:
            sides[force_side] = []

        if force_user not in sides[force_side]:
            sides[force_side].append(force_user)
    elif ">" in data:
        force_user, force_side = data.split(" -> ")

        if force_side not in sides:
            sides[force_side] = []

        for side_one in sides.keys():
            if force_user in sides[side_one]:
                sides[side_one].remove(force_user)
                sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
                break

        all_values = []
        for side_two in sides.values():
            for name_one in side_two:
                all_values.append(name_one)

        if force_user not in all_values:
            sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")


sides = {}

while True:
    data = input()

    if data == "Lumpawaroo":
        break

    check_type_of_input(data)

sides = sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]))

for side, name in sides:
    if len(name) > 0:
        print(f"Side: {side}, Members: {len(name)}")
        name = sorted(name)

        for current_name in name:
            print(f"! {current_name}")
