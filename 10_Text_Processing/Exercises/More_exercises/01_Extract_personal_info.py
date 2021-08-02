number = int(input())

name = ""
age = ""

for i in range(number):
    data = input()
    index = 0

    while True:
        if index >= len(data):
            break
        if data[index] == "@":

            while True:
                index += 1
                if data[index] == "|":
                    break
                name += data[index]
        elif data[index] == "#":

            while True:
                index += 1
                if data[index] == "*":
                    break
                age += data[index]
        index += 1

    if name != "" and age != "":
        print(f"{name} is {age} years old.")
        name = ""
        age = ""