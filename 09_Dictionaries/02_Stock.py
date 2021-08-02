products = input().split()

available_products = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]

    available_products[key] = value

searched_products = input().split()

for item in searched_products:
    if item in available_products.keys():
        print(f"We have {available_products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")