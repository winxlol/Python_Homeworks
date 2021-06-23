COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

product = input()
price = int(input())


def order_price(product, price):
    if product == "coffee":
        return COFFEE * price
    elif product == "water":
        return WATER * price
    elif product == "coke":
        return COKE * price
    elif product == "snacks":
        return SNACKS * price


total_order = order_price(product, price)
print(f"{total_order:.2f}")