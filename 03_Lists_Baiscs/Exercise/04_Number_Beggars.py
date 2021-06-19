treasure = input().split(", ")
beggars = int(input())

list_of_beggars = []

for beggar in range(beggars):
    list_of_beggars.append(0)

index = 0

for current_treasure in treasure:
    current_treasure = int(current_treasure)
    if index == len(list_of_beggars):
        index = 0
        list_of_beggars[index] += current_treasure
    else:
        list_of_beggars[index] += current_treasure
    index += 1

print(list_of_beggars)