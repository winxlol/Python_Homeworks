factor = int(input())
count = int(input())

multiples_numbers = []

for number in range(1, count + 1):
    multiples_numbers.append(number * factor)

print(multiples_numbers)