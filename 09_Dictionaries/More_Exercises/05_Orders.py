orders = {}

while True:
    products = input().split()

    buy_command = products[0]

    if buy_command == "buy":
        break

    name = products[0]
    price = float(products[1])
    quantity = float(products[2])

    if name not in orders:
        orders[name] = [price, quantity]

    else:
        orders[name][1] += quantity
        orders[name][0] = price

#for current_order in orders:
#    price_info = orders[current_order][0]
#    quantity_info = orders[current_order][1]
#
#    total_price = price_info * quantity_info
#
#    print(f"{current_order} -> {total_price:.2f}")

for product in orders:
    for price in product:
        print(price)