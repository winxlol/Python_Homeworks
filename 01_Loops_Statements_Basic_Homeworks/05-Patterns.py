number = int(input())

for i in range(number):
    for k in range(i + 1):
        print("*", end="")
    print(end="\n")

for j in range(number):
    number -= 1
    for n in range(number, 0, -1):
        print("*", end="")
    print(end="\n")
