def collect(item):
    if item not in collected_items:
        collected_items.append(item)


def drop(item):
    if item in collected_items:
        collected_items.remove(item)


def combine_items(old_item, new_item):
    for index, current_item in enumerate(collected_items):
        if old_item == current_item:
            collected_items.insert(index + 1, new_item)


def renew(item):
    if item in collected_items:
        index_item = collected_items.index(item)
        collected_items.pop(index_item)
        collected_items.append(item)


collected_items = input().split(", ")

while True:
    commands = input()

    if commands == "Craft!":
        break

    tokens = commands.split(" - ")
    type_command = tokens[0]

    if type_command == "Collect":
        item = tokens[1]
        collect(item)
    elif type_command == "Drop":
        item = tokens[1]
        drop(item)
    elif type_command == "Combine Items":
        items = tokens[1].split(":")
        old_item = items[0]
        new_item = items[1]
        combine_items(old_item, new_item)
    elif type_command == "Renew":
        item = tokens[1]

        renew(item)


print(", ".join(collected_items))