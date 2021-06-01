ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

quantity = int(input())
days_left = int(input())
is_third_day = False

budget = 0
christmas_spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ORNAMENT_SET * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        budget += (TREE_SKIRT * quantity) + (TREE_GARLANDS * quantity)
        christmas_spirit += 13
        is_third_day = True
    if day % 5 == 0:
        budget += TREE_LIGHTS * quantity
        christmas_spirit += 17
        if is_third_day:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS
        if day == days_left:
            christmas_spirit -= 30
    is_third_day = False


print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
