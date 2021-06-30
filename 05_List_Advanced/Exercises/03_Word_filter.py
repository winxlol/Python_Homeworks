data = input().split()

result = [el for el in data if len(el) % 2 == 0]

for element in result:
    print(element)