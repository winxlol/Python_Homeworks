from collections import defaultdict
collections = defaultdict(int)

while True:
    data = input()

    if data == "statistics":
        break

    key, value = data.split(": ")
    value = int(value)

    collections[key] += value

print("Products in stock:")
for key, value in collections.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(collections)}")
print(f"Total Quantity: {sum(collections.values())}")