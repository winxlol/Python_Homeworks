data = input().split()

bakary_products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = data[index + 1]
    bakary_products[key] = int(value)

print(bakary_products)