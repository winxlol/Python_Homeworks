sequence_numbers = input().split()
string_chars = list(input())

final_message = []


for number in sequence_numbers:

    sum_of_current_number = 0

    for current_number in number:
        current_number = int(current_number)
        sum_of_current_number += current_number

    number_index = 0
    while True:
        is_need_break = False
        current_index = 0
        for char in string_chars:
            if current_index > len(string_chars):
                break
            if number_index == sum_of_current_number:
                is_need_break = True
                final_message.append(char)
                string_chars.pop(current_index)
                break
            current_index += 1
            number_index += 1
        if is_need_break:
            number_index = 0
            break

print("".join(final_message))
