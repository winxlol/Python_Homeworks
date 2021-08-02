data = input()

for index, char in enumerate(data):
    if char == ":" and data[index + 1] != " ":
        print(char + data[index + 1])
