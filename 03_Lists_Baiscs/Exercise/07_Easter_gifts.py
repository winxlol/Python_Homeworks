gifts_collection = input().split()

while True:
    data = input()

    if data == "No Money":
        break

    commands = data.split()

    command = commands[0]
    gift = commands[1]

    if len(commands) > 2:
        index = int(commands[2])

    if command == "OutOfStock":
        for current_index, item in enumerate(gifts_collection):
            if item == gift:
                gifts_collection[current_index] = "None"
    elif command == "Required":
        if 0 <= index < len(gifts_collection):
            gifts_collection[index] = gift
    elif command == "JustInCase":
        gifts_collection[-1] = gift

final_result = []

for current_gift in gifts_collection:
    if not current_gift == "None":
        final_result.append(current_gift)

print(" ".join(final_result))


