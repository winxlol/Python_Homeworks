data = input()

temp_string = ""
temp_number = ""

final_string = ""


for index, char in enumerate(data):
    if not char.isdigit():
        temp_string += char

    if char.isdigit():
        if index + 1 < len(data) and data[index + 1].isdigit():
            temp_number += char
            continue

        temp_number += char
        final_string += temp_string.upper() * int(temp_number)
        temp_string = ""
        temp_number = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)