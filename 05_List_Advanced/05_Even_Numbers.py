numbers = list(map(int, input().split(", ")))

even_numbers = [el for el in range(len(numbers)) if numbers[el] % 2 == 0]

print(even_numbers)
