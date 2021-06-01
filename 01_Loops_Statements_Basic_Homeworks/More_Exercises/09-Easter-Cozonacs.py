budget = float(input())
flour_kg_price = float(input())

eggs_pack_price = flour_kg_price * 0.75
milk_litre_price = flour_kg_price * 1.25

cozonac_price = flour_kg_price + eggs_pack_price + (milk_litre_price / 4)

cozonac_amount = 0
colored_eggs = 0

while budget >= cozonac_price:
    cozonac_amount += 1
    colored_eggs += 3

    if cozonac_amount % 3 == 0:
        colored_eggs -= cozonac_amount - 2

    budget -= cozonac_price

print(f"You made {cozonac_amount} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
