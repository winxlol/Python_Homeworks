from collections import defaultdict

items_collection = {'Shadowmourne': {'shards': 0}, 'Valanyr': {'fragments': 0}, 'Dragonwrath': {'motes': 0}}
junk_collection = defaultdict(int)

is_win = False


while True:
    data = input().split()

    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item == 'shards':
            items_collection['Shadowmourne']['shards'] += quantity

            if items_collection['Shadowmourne']['shards'] >= 250:
                print("Shadowmourne obtained!")
                items_collection['Shadowmourne']['shards'] -= 250
                is_win = True
                break
        elif item == 'fragments':
            items_collection['Valanyr']['fragments'] += quantity

            if items_collection['Valanyr']['fragments'] >= 250:
                print("Valanyr obtained!")
                items_collection['Valanyr']['fragments'] -= 250
                is_win = True
                break
        elif item == 'motes':
            items_collection['Dragonwrath']['motes'] += quantity

            if items_collection['Dragonwrath']['motes'] >= 250:
                print("Dragonwrath obtained!")
                items_collection['Dragonwrath']['motes'] -= 250
                is_win = True
                break
        else:
            junk_collection[item] += quantity

    if is_win:
        break


print(items_collection)
print(junk_collection)

