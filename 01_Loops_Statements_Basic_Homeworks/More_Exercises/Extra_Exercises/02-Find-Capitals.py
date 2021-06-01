text = input()

indices_list = []


for index, letter in enumerate(text):
    if letter.isupper():
        indices_list.append(index)

print(indices_list)