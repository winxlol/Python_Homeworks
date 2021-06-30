numbers = list(map(int, input().split(", ")))

group = 10
last_group = 0

while not len(numbers) == 0:
    list_numbers = [el for el in numbers if last_group < el <= group]

    print(f"Group of {group}'s: {list_numbers}")

    for number in list_numbers:
        if number in numbers:
            numbers.remove(number)

    group += 10
    last_group += 10

