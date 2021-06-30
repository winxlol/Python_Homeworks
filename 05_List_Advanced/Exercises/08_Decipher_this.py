words = input().split()

decrepted_list = []

for word in words:
    digit = ''
    temp_list = []
    for letter in word:
        if letter.isdigit():
            digit += letter
        else:
            temp_list.append(letter)

    digit = int(digit)

    temp_list.insert(0, chr(digit))
    temp_list[1], temp_list[-1] = temp_list[-1], temp_list[1]

    decrepted_list.append("".join(temp_list))

print(" ".join(decrepted_list))