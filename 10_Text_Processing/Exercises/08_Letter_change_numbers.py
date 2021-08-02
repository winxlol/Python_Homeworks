def first_letter_uppercase_or_lowercase(first_letter, number):
    if first_letter.isupper():
        return number / (ord(first_letter) - 64)
    elif first_letter.islower():
        return number * (ord(first_letter) - 96)


def last_letter_uppercase_or_lowercase(last_letter, number):
    if last_letter.isupper():
        return number - (ord(last_letter) - 64)
    elif last_letter.islower():
        return number + (ord(last_letter) - 96)


data = input().split()

total_sum = 0

for current_data in data:
    first_letter = current_data[0]
    last_letter = current_data[-1]
    given_number = float(current_data[1:-1])

    resulted_number_first_letter = first_letter_uppercase_or_lowercase(first_letter, given_number)
    resulted_number_last_letter = last_letter_uppercase_or_lowercase(last_letter, resulted_number_first_letter)

    total_sum += resulted_number_last_letter

print(f"{total_sum:.2f}")




