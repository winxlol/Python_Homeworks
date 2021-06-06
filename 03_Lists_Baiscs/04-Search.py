attempts = int(input())
word = input()

list_of_strings = []
filtred_strings = []

for attempt in range(attempts):
    current_string = input()
    list_of_strings.append(current_string)

    if word in current_string:
        filtred_strings.append(current_string)

print(list_of_strings)
print(filtred_strings)
