first_char = input()
second_char = input()

data = input()

first_char_index = ord(first_char)
second_char_index = ord(second_char)

min_number = min(first_char_index, second_char_index)
max_number = max(first_char_index, second_char_index)

total_sum = 0

for char in data:
    if min_number < ord(char) < max_number:
        total_sum += ord(char)

print(total_sum)