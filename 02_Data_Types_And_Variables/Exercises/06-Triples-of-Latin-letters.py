number = int(input())

ascii_letter = 97


for n in range(number):
    current_char_first = ascii_letter + n
    for j in range(number):
        current_char_second = ascii_letter + j
        for k in range(number):
            current_char_third = ascii_letter + k
            print(chr(current_char_first) + chr(current_char_second) + chr(current_char_third))

