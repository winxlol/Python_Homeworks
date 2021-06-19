attempts = int(input())

store_numbers_list = []

for attempt in range(attempts):
    current_number = int(input())
    store_numbers_list.append(current_number)

filtred_numbers = []

command = input()

if command == 'even':
    filtred_numbers = [number for number in store_numbers_list if number % 2 == 0]
elif command == "odd":
    filtred_numbers = [number for number in store_numbers_list if number % 2 == 1]
elif command == "negative":
    filtred_numbers = [number for number in store_numbers_list if number < 0]
elif command == "positive":
    filtred_numbers = [number for number in store_numbers_list if number >= 0]

print(filtred_numbers)
