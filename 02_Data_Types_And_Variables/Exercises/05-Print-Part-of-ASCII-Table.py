start_number = int(input())
finish_number = int(input())

for current_char in range(start_number, finish_number + 1):
    ascii_char = chr(current_char)
    print(ascii_char, end=" ")

