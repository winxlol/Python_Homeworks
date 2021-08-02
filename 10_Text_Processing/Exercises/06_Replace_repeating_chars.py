data = input()

current_char = ""
final_result = ""

for index, char in enumerate(data):
    if index + 1 == len(data):
        if char == data[index]:
            final_result += char
        else:
            final_result += char
        break
    current_char += char

    if data[index + 1] == char:
        continue
    else:
        final_result += char
        current_char = ""

print(final_result)