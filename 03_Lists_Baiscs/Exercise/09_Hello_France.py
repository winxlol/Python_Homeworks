CLOTHES = 50
SHOES = 35
ACCESSORIES = 20.50
PRICE_TICKETS = 150

items_collection = input().split("|")
budget = float(input())

bought_items = []

for current_item in items_collection:
    type_item, price_item = current_item.split("->")

    price_item = float(price_item)

    if budget >= price_item:
        if type_item == "Clothes":
            if price_item <= CLOTHES:
                budget -= price_item
                bought_items.append(price_item)
        elif type_item == "Shoes":
            if price_item <= SHOES:
                budget -= price_item
                bought_items.append(price_item)
        elif type_item == "Accessories":
            if price_item <= ACCESSORIES:
                budget -= price_item
                bought_items.append(price_item)

new_price_items = list(map(lambda a: a * 1.40, bought_items))

profit = sum(new_price_items) - sum(bought_items)
new_budget = sum(new_price_items) + budget

for item in new_price_items:
    print(f"{item:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if new_budget >= PRICE_TICKETS:
    print("Hello, France!")
else:
    print("Time to go.")
