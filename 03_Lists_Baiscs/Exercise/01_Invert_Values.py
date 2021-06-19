numbers = input().split()

reversed_numbers = []

for number in numbers:
    number = int(number)
    if number >= 0:
        reversed_number = number - (number * 2)
        reversed_numbers.append(reversed_number)
    else:
        reversed_number = number + (-number * 2)
        reversed_numbers.append(reversed_number)

print(reversed_numbers)