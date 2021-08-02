from collections import defaultdict

mine_resource = defaultdict(int)

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    mine_resource[resource] += quantity

mine_resource = dict(sorted(mine_resource.items(), key=lambda x: (x[0], x[1])))

for key, value in mine_resource.items():
    print(f"{key} -> {value}")