KIDS = "toddy"
TEENS = "coke"
YOUNG_ADULTS = "beer"
ADULTS = "whisky"

age = int(input())

if age <= 14:
    print(f"drink {KIDS}")
elif age <= 18:
    print(f"drink {TEENS}")
elif age <= 21:
    print(f"drink {YOUNG_ADULTS}")
else:
    print(f'drink {ADULTS}')
