first_string = input()
second_string = input()

list_first_string = []

for char in first_string:
    list_first_string.append(char)


for index, letter in enumerate(second_string):
    if letter != list_first_string[index]:
        list_first_string[index] = letter
        print("".join(list_first_string))