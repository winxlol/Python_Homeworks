first_sequences = input().split(", ")
second_sequences = input().split(", ")

new_list = []

is_substring = False

for substring in first_sequences:
    for word in second_sequences:
        if substring in word:
            is_substring = True
    if is_substring:
        new_list.append(substring)
        is_substring = False


print(new_list)
