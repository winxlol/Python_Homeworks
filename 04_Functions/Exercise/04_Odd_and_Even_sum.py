def even(data):
    sum_even = 0

    for current_char in data:
        parse_to_int = int(current_char)

        if parse_to_int % 2 == 0:
            sum_even += parse_to_int

    return sum_even


def odd(data):
    sum_odd = 0

    for current_char in data:
        parse_to_int = int(current_char)

        if parse_to_int % 2 == 1:
            sum_odd += parse_to_int

    return sum_odd


data = input()

sum_even_numbers = even(data)
sum_odd_numbers = odd(data)

print(f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}")